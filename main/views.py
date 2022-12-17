import datetime
import re
import json

import pytz
import pendulum
import dateutil.parser
from dateutil import relativedelta

from django import urls, shortcuts, http
from django import forms as django_forms
from django.contrib import messages
from django.views import generic
from django.utils.translation import gettext as _
from django.utils import timezone
from django.template.response import TemplateResponse

from . import models, forms, utils


CONSTANTS = {
    'PAGINATE_BY': 12
}


# Mixins
class IncrementViewCount:

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count = obj.view_count + 1
        obj.save()
        return obj


class FilterLanguageMixin:
    def get_queryset(self):
        return self.model.objects.filter(translations__language_code=self.request.LANGUAGE_CODE)


# Views
class TemplateResponseForbidden(TemplateResponse):
    status_code = 404


class NotFoundTemplateView(generic.TemplateView):
    response_class = TemplateResponseForbidden
    template_name = "pages/not_found.html"
    status = 404


class HomeTemplate(generic.TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)

        c['banners'] = models.Banner.objects.filter(translations__language_code=self.request.LANGUAGE_CODE)
        c['posts'] = models.Post.published().filter(translations__language_code=self.request.LANGUAGE_CODE)[:3]
        c['festivals'] = models.Album.objects.filter(translations__language_code=self.request.LANGUAGE_CODE)[:8]
        c['medias'] = models.Media.objects.filter(translations__language_code=self.request.LANGUAGE_CODE, category='photo')[:8]
        c['useful_links'] = models.UsefulLink.objects.filter(translations__language_code=self.request.LANGUAGE_CODE)
        c['key_indicators'] = models.KeyIndicator.objects.filter(translations__language_code=self.request.LANGUAGE_CODE)
        c['last_album'] = models.Album.objects.filter(translations__language_code=self.request.LANGUAGE_CODE).order_by('time_added').last()

        today = datetime.date.today()
        now = datetime.datetime.now(tz=pytz.timezone(timezone.get_current_timezone_name()))
        c['calendar_event'] = {
            "event": models.Event.objects.filter(
                translations__language_code=self.request.LANGUAGE_CODE,
                event_type='event',
                start_date__gte=now
            )[:2],
            "exhibition": models.Event.objects.filter(
                translations__language_code=self.request.LANGUAGE_CODE,
                event_type='exhibition',
                start_date__gte=now
            )[:2],
            "dates": list(set([
                date.start_date.strftime('%Y-%m-%d') for date in models.Event.objects.filter(
                    start_date__date__gte=today + relativedelta.relativedelta(months=-1),
                    start_date__date__lte=today + relativedelta.relativedelta(months=+1),
                )
            ]))
        }
        c['upcoming_events'] = {
            "upcoming": models.Event.objects.filter(
                translations__language_code=self.request.LANGUAGE_CODE,
                start_date__date=datetime.date.today()
            )[:3],
            "current": models.Event.objects.filter(
                translations__language_code=self.request.LANGUAGE_CODE,
                start_date__date=datetime.date.today()
            )[:3],
            "past": models.Event.objects.filter(
                translations__language_code=self.request.LANGUAGE_CODE,
                start_date__date__lt=datetime.date.today()
            )[:3],
        }

        settings = models.SiteSettings.objects.first()
        stat_data = models.StatisticalData.objects.all()

        c['statistic_data'] = {}

        for field in ['accepted', 'on_process', 'solved', 'not_solved']:
            c['statistic_data'][field] = getattr(settings, f'statistics_{ field }') + (
                sum([v[f'helpline_{ field }'] for v in stat_data.values(f'helpline_{ field }')]) +
                sum([v[f'online_{ field }'] for v in stat_data.values(f'online_{ field }')]) +
                sum([v[f'oral_{ field }'] for v in stat_data.values(f'oral_{ field }')]) +
                sum([v[f'written_{ field }'] for v in stat_data.values(f'written_{ field }')])
            )

        return c


class StaticDetail(IncrementViewCount, FilterLanguageMixin, generic.DetailView):
    template_name = "pages/static/detail.html"
    model = models.Static
    context_object_name = "static"
    pk_url_kwarg = 'id'


class PersonList(FilterLanguageMixin, generic.ListView):
    template_name = "pages/person/list.html"
    model = models.Person
    context_object_name = "persons"
    paginate_by = CONSTANTS['PAGINATE_BY']

    def get_queryset(self):
        if self.request.GET.get('not_primary_staff', False) in (1, '1', 'true', 'True', True):
            return super().get_queryset().filter(not_primary_staff=True)
        return super().get_queryset().filter(not_primary_staff=False)


class PersonDetail(IncrementViewCount, FilterLanguageMixin, generic.DetailView):
    template_name = "pages/person/detail.html"
    model = models.Person
    context_object_name = "person"
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        if not (self.request.GET.get('not_primary_staff', False) in (1, '1', 'true', 'True', True)):
            return super().get_object(queryset)


class ApplicationForm(generic.FormView, generic.CreateView):
    template_name = "pages/application_form.html"
    form_class = forms.ApplicationForm
    context_object_name = "form"

    def form_invalid(self, form):
        print("invalid")
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        print("---------------------------valid---------------------------")
        email_sent = utils.send_email(self.request, form)
        print(f"---------------------------email_sent: { email_sent }---------------------------")
        return super().form_valid(form)

    def get_success_url(self):
        print("success_url")
        messages.add_message(
            request=self.request,
            level=messages.SUCCESS,
            message=_("Your application received successfully")
        )
        return urls.reverse('application_form')


class ContactPage(generic.TemplateView):
    template_name = "pages/contact.html"

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['about_page_data'] = models.AboutPageData.objects.filter(translations__language_code=self.request.LANGUAGE_CODE).first()
        return c


class EventList(FilterLanguageMixin, generic.ListView):
    template_name = "pages/event/list.html"
    model = models.Event
    context_object_name = "events"

    def get_context_data(self, *, object_list=None, **kwargs):
        c = super().get_context_data(object_list=object_list, **kwargs)

        if self.request.GET.get('date', False) and re.match(r'\d{4}-\d{2}-\d{2}', self.request.GET.get('date')):
            date = dateutil.parser.parse(self.request.GET.get('date'))
        else:
            date = datetime.date.today()

        today = pendulum.today()

        prev_month_start = (today.subtract(months=1).start_of('month'))
        next_month_end = (today.add(months=1).end_of('month'))

        qs = self.model.objects.filter(
            translations__language_code=self.request.LANGUAGE_CODE,
        )

        c['calendar_event'] = {
            'event': qs.filter(
                event_type='event',
                start_date__year=date.year,
                start_date__month=date.month,
                start_date__day=date.day,
            ),
            'exhibition': qs.filter(
                event_type='exhibition',
                start_date__year=date.year,
                start_date__month=date.month,
                start_date__day=date.day,
            ),
            "dates": [event.start_date.strftime('%Y-%m-%d') for event in qs.filter(
                start_date__year__gte=prev_month_start.year,
                start_date__month__gte=prev_month_start.month,
                start_date__day__gte=prev_month_start.day,
                start_date__year__lte=next_month_end.year,
                start_date__month__lte=next_month_end.month,
                start_date__day__lte=next_month_end.day,
            )]
        }

        return c


class EventDetail(IncrementViewCount, FilterLanguageMixin, generic.DetailView, generic.FormView, generic.CreateView):
    template_name = "pages/event/detail.html"
    model = models.Event
    form_class = forms.EventForm
    context_object_name = "event"
    pk_url_kwarg = "id"

    def form_invalid(self, form):
        messages.add_message(
            request=self.request,
            level=messages.ERROR,
            message=_("Invalid data sent")
        )
        self.object = self.get_object()
        return super().form_invalid(form)

    def form_valid(self, form):
        utils.send_email(self.request, form)
        messages.add_message(
            request=self.request,
            level=messages.SUCCESS,
            message=_("Your order received successfully")
        )
        return super().form_valid(form)

    def get_success_url(self):
        return urls.reverse('event_detail', args=[self.object.event.id])


class PostList(FilterLanguageMixin, generic.ListView):
    template_name = "pages/post/list.html"
    model = models.Post
    context_object_name = "posts"
    paginate_by = CONSTANTS['PAGINATE_BY']

    def get_context_data(self, *, object_list=None, **kwargs):
        c = super().get_context_data(object_list=object_list, **kwargs)

        if self.request.GET.get('category_id', False):
            cat = models.PostCategory.objects.filter(
                translations__language_code=self.request.LANGUAGE_CODE,
                id=self.request.GET.get('category_id')
            )

            if cat.count():
                c['category'] = cat[0]
        return c

    def get_queryset(self):
        kws = {}
        params = self.request.GET

        if params.get('category_id', False):
            kws['post_category__in'] = params.get('category_id')

        return super().get_queryset().filter(**kws).order_by('-posting_date')


class PostDetail(IncrementViewCount, FilterLanguageMixin, generic.DetailView):
    template_name = "pages/post/detail.html"
    model = models.Post
    context_object_name = "post"
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)

        obj = self.object
        if obj:
            if obj.post_category.first():
                c['other_posts'] = obj.post_category.first().post_set.all().exclude(id=obj.id)[:10]

        return c


class OrganizationList(FilterLanguageMixin, generic.ListView):
    template_name = "pages/organization/list.html"
    model = models.Organization
    context_object_name = "organizations"
    paginate_by = CONSTANTS['PAGINATE_BY']

    def get_context_data(self, *, object_list=None, **kwargs):
        c = super().get_context_data(object_list=object_list, **kwargs)

        c['regions'] = models.OrganizationRegion.objects.filter(parent__isnull=True, translations__language_code=self.request.LANGUAGE_CODE)

        if self.request.GET.get('category_id', False):
            cat = models.OrganizationCategory.objects.filter(
                translations__language_code=self.request.LANGUAGE_CODE,
                id=self.request.GET.get('category_id')
            )

            if cat.count():
                c['category'] = cat[0]

        return c

    def get_queryset(self):
        kws = {
            "translations__language_code": self.request.LANGUAGE_CODE
        }

        params = self.request.GET

        if params.get('category_id', False):
            kws['organization_category'] = params.get('category_id')

        if params.get('region_id', False):
            region_id = params.get('region_id')

            if str(region_id).isnumeric() and int(region_id) != 0:
                kws['region_id'] = region_id

        return super().get_queryset().filter(**kws).order_by('-view_count')


class OrganizationDetail(IncrementViewCount, FilterLanguageMixin, generic.DetailView):
    template_name = "pages/organization/detail.html"
    model = models.Organization
    context_object_name = "organization"
    pk_url_kwarg = 'id'


class AlbumList(FilterLanguageMixin, generic.ListView):
    template_name = "pages/album/list.html"
    model = models.Album
    context_object_name = 'albums'

    def get_queryset(self):
        params = {}

        if self.request.GET.get('category', False):
            params['category'] = self.request.GET.get('category')

        return super().get_queryset().filter(**params)


class AlbumDetail(IncrementViewCount, FilterLanguageMixin, generic.DetailView):
    template_name = "pages/album/detail.html"
    model = models.Album
    context_object_name = 'album'
    pk_url_kwarg = 'id'


class RegionsList(generic.TemplateView):
    template_name = "pages/region/region.html"

    def get_context_data(self, **kwargs):
        c = super(RegionsList, self).get_context_data(**kwargs)

        c['regions'] = models.RegionalOffice.objects.filter(translations__language_code=self.request.LANGUAGE_CODE)

        orgs = []

        for region in models.OrganizationRegion.objects.filter(translations__language_code=self.request.LANGUAGE_CODE):
            organizations = region.organization_set.filter(translations__language_code=self.request.LANGUAGE_CODE)
            org = {
                "region_name": region.name,
                "organizations": organizations
            }

            if organizations:
                orgs.append(org)

        c['organizations'] = orgs

        return c


class MediaTemplate(FilterLanguageMixin, generic.TemplateView):
    template_name = "pages/media/index.html"


class MediaGalleryList(FilterLanguageMixin, generic.ListView):
    template_name = "pages/media/list.html"
    model = models.Media
    context_object_name = 'medias'

    def get_queryset(self):
        params = {}

        if self.request.GET.get('category', False):
            params['category'] = self.request.GET.get('category')

        return super().get_queryset().filter(**params)


class MediaGalleryDetail(IncrementViewCount, FilterLanguageMixin, generic.DetailView):
    template_name = "pages/media/detail.html"
    model = models.Media
    context_object_name = 'media'
    pk_url_kwarg = 'id'


class StatisticsList(FilterLanguageMixin, generic.TemplateView):
    template_name = "pages/statistics/list.html"
    model = models.StatisticalData

    def get_context_data(self, *, object_list=None, **kwargs):
        c = super().get_context_data(object_list=object_list, **kwargs)

        def get_sum_of_stats(key, stats):
            return sum([getattr(stat, key) for stat in stats])

        kws = {}

        if self.request.GET.get('start_date', False) and self.request.GET.get('end_date', False):
            filter_date_range = []

            if self.request.GET.get('start_date', False):
                start_date = f"{ self.request.GET.get('start_date') }-01".split('-')
                filter_date_range.append(
                    pendulum.date(
                        int(start_date[0].lstrip('0')),
                        int(start_date[1].lstrip('0')),
                        int(start_date[2].lstrip('0'))
                    ).start_of('month')
                )
                kws['month__gte'] = filter_date_range[0]

            if self.request.GET.get('end_date', False):
                end_date = f"{ self.request.GET.get('end_date') }-01".split('-')
                filter_date_range.append(
                    pendulum.date(
                        int(end_date[0].lstrip('0')),
                        int(end_date[1].lstrip('0')),
                        int(end_date[2].lstrip('0'))
                    ).end_of('month')
                )
                kws['month__lte'] = filter_date_range[1]
        elif self.request.GET.get('start_date', False) or self.request.GET.get('end_date', False):
            c['need_to_fill_both_dates'] = True
        else:
            kws = {}

        stats = self.model.objects.filter(**kws)

        c['data'] = {
            "written": {
                "received_and_on_process": (get_sum_of_stats('written_accepted', stats) + get_sum_of_stats('written_on_process', stats)),
                "completed": get_sum_of_stats('written_solved', stats),
                "invalid": get_sum_of_stats('written_not_solved', stats),
            },
            "oral": {
                "received_and_on_process": (get_sum_of_stats('oral_accepted', stats) + get_sum_of_stats('oral_on_process', stats)),
                "completed": get_sum_of_stats('oral_solved', stats),
                "invalid": get_sum_of_stats('oral_not_solved', stats),
            },
            "helpline": {
                "received_and_on_process": (get_sum_of_stats('helpline_accepted', stats) + get_sum_of_stats('helpline_on_process', stats)),
                "completed": get_sum_of_stats('helpline_solved', stats),
                "invalid": get_sum_of_stats('helpline_not_solved', stats),
            },
            "online": {
                "received_and_on_process": (get_sum_of_stats('online_accepted', stats) + get_sum_of_stats('online_on_process', stats)),
                "completed": get_sum_of_stats('online_solved', stats),
                "invalid": get_sum_of_stats('online_not_solved', stats),
            },
        }

        all_x = {}
        all_x['all_received_and_on_process'] = sum([c['data'][k]['received_and_on_process'] for k in c['data']])
        all_x['all_completed'] = sum([c['data'][k]['completed'] for k in c['data']])
        all_x['all_invalid'] = sum([c['data'][k]['invalid'] for k in c['data']])

        all_y = {
            "written": 0,
            "oral": 0,
            "helpline": 0,
            "online": 0,
        }
        for k in c['data']:
            for l in c['data'][k]:
                all_y[k] += int(c['data'][k][l])

        c['data']['all_x'] = all_x
        c['data']['all_y'] = all_y

        return c


class TypoReportAPI(generic.FormView):
    form_class = forms.TypoReportingForm
    template_name = 'parts/empty.html'

    def get(self, request, *args, **kwargs):
        return shortcuts.redirect('/')

    def post(self, request, *args, **kwargs):
        form = self.form_class(json.loads(request.body))
        if form.is_valid():
            form.save()
            return http.JsonResponse({'status': 'OK'}, status=200)
        else:
            return http.JsonResponse({'status': 'Error'}, status=400)


class SearchTemplateView(generic.ListView):
    template_name = 'pages/search.html'
    models = [
        models.Event,
        models.Person,
        models.Post,
        models.Organization,
        models.Media,
        models.Album,
    ]

    fields = [
        'title',
        'description',
        'content',
        'full_name',
        'position',
        'short_description',
        'body',
    ]

    def get_queryset(self):
        from itertools import chain
        qs = []

        for model in self.models:
            qs += list(chain(model.objects.filter(translations__language_code=self.request.LANGUAGE_CODE).distinct()))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchTemplateView, self).get_context_data(object_list=object_list, **kwargs)

        res = []
        s = self.request.GET.get('search')

        if s:
            for obj in self.get_queryset():

                existing_fields = []

                existing_fields.append('title') if hasattr(obj, 'title') else ''
                existing_fields.append('description') if hasattr(obj, 'description') else ''
                existing_fields.append('content') if hasattr(obj, 'content') else ''
                existing_fields.append('full_name') if hasattr(obj, 'full_name') else ''
                existing_fields.append('position') if hasattr(obj, 'position') else ''
                existing_fields.append('short_description') if hasattr(obj, 'short_description') else ''
                existing_fields.append('body') if hasattr(obj, 'body') else ''

                for field in existing_fields:

                    o = django_forms.model_to_dict(obj)
                    if hasattr(o, field):
                        if str(s).lower() in str(o[field]).lower():
                            res.append(obj)
                    else:

                        try:
                            s_in = obj.safe_translation_getter(field) if obj.safe_translation_getter(field) else ''
                        except:
                            s_in = o[field]

                        if str(s).lower() in str(s_in).lower():
                            if obj not in res:
                                res.append(obj)

            ret = []

            # Add link
            for o in res:
                existing_fields = []

                existing_fields.append('title') if hasattr(o, 'title') else ''
                existing_fields.append('name') if hasattr(o, 'name') else ''
                existing_fields.append('full_name') if hasattr(o, 'full_name') else ''

                for field in existing_fields:
                    c = o._meta.verbose_name

                    if ":" in str(c) and len(str(c).split(':')) >= 1:
                        cat = str(c).split(':')[1:][0]
                    else:
                        cat = str(c)

                    if hasattr(o, field):
                        tit = getattr(o, field)
                    else:
                        tit = o.safe_translation_getter(field)

                    ret.append({
                        "title": tit,
                        "link": o.get_absolute_url(),
                        "type": cat
                    })

            retr = {}
            for r in ret:

                if r['type'] not in retr.keys():
                    retr[r['type']] = [r]
                else:
                    retr[r['type']].append(r)

            # context['items'] = ret
            context['types'] = retr
        else:
            context['types'] = []

        return context
