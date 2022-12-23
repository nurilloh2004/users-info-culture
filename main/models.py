import datetime

import pytz
from django import urls
from django.core import exceptions as django_core_exceptions
from django.core import validators as django_core_validators
from django.db import models
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _lazy, ugettext as _
from django.utils import timezone

from ckeditor import fields as ckeditor_fields
from ckeditor_uploader import fields as ckeditor_uploader_fields
from geoposition import fields as geoposition_fields
from mptt import models as mptt_models
from parler import models as parler_models

from . import managers


# Constants
LIST_EVENT_TYPES = (
    ('event', _lazy('Event')),
    ('exhibition', _lazy('Exhibition')),
)

LIST_REGIONS = (
    ('andijan', _lazy("Andijan")),
    ('bukhara', _lazy("Bukhara")),
    ('fergana', _lazy("Fergana")),
    ('jizzakh', _lazy("Jizzakh")),
    ('karakalpakstan', _lazy("Karakalpakstan")),
    ('kashkadarya', _lazy("Kashkadarya")),
    ('khorezm', _lazy("Khorezm")),
    ('namangan', _lazy("Namangan")),
    ('navoi', _lazy("Navoi")),
    ('samarkand', _lazy("Samarkand")),
    ('surkhandarya', _lazy("Surkhandarya")),
    ('syrdarya', _lazy("Syrdarya")),
    ('tashkent_city', _lazy("Tashkent city")),
    ('tashkent_region', _lazy("Tashkent region")),
)


# Mixins
class ViewCountMixin(models.Model):
    view_count = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        abstract = True


class OrderMixin(models.Model):
    order = models.PositiveIntegerField(default=0, blank=False, null=False, editable=False)

    class Meta:
        abstract = True
        ordering = ['order']


class AddedUpdatedDateTimeMixin(models.Model):
    time_added = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    time_updated = models.DateTimeField(auto_now=True, editable=False, null=True)

    class Meta:
        abstract = True


class AddedUpdatedEditableDateTimeMixin(models.Model):
    time_added = models.DateTimeField(auto_now_add=True, editable=True)
    time_updated = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        abstract = True


# Models

class Banner(OrderMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255, null=True, blank=True),
        link=models.CharField(max_length=1000, null=True, blank=True),
    )
    image = models.FileField(upload_to="uploads/banner/")

    class Meta:
        ordering = ['order']
        verbose_name = _lazy("Banner")
        verbose_name_plural = _lazy("Banners")

    def __str__(self): return f"{ self.safe_translation_getter('title', self.id) }"


class Menu(mptt_models.MPTTModel, parler_models.TranslatableModel):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    translations = parler_models.TranslatedFields(
        name=models.CharField(blank=False, max_length=128),
        link=models.CharField(blank=True, null=True, max_length=128)
    )
    display_in_main_menu = models.BooleanField(default=False)
    objects = managers.CustomMpttManager()

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or ''

    class Meta:
        verbose_name = _lazy("Menu item")
        verbose_name_plural = _lazy("Menu items")


class Event(ViewCountMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255),
        description=models.CharField(max_length=255),
        content=ckeditor_uploader_fields.RichTextUploadingField(),
        note=models.CharField(max_length=255, null=True, blank=True),
        address=models.CharField(max_length=500, null=True),
        organizer=models.CharField(max_length=255, null=True, blank=True),
    )
    image = models.ImageField(upload_to="uploads/event/%Y/%m/%d", default="defaults/event.png")
    event_type = models.CharField(max_length=255, choices=LIST_EVENT_TYPES)

    price = models.IntegerField(null=True, blank=True)
    location = geoposition_fields.GeopositionField(null=True)

    start_date = models.DateTimeField(editable=True, null=True)
    end_date = models.DateTimeField(editable=True, null=True)

    class Meta:
        ordering = ['start_date']
        verbose_name = _lazy("Event")
        verbose_name_plural = _lazy("Events")

    def __str__(self): return f"{ self.safe_translation_getter('title', str(self.id)) }"

    def get_absolute_url(self): return urls.reverse('event_detail', args=[self.id])


class EventOrder(AddedUpdatedDateTimeMixin):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    people_count = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _lazy("Event order")
        verbose_name_plural = _lazy("Event orders")

    def __str__(self): return f"{ self.event.safe_translation_getter('title', str(self.id)) }"


class SiteSettings(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        event_contact_info=ckeditor_fields.RichTextField(config_name='basic', null=True),
        address=models.CharField(max_length=255, null=True),
        email=models.EmailField(null=True),
        tel=models.CharField(max_length=255, null=True),
        work_hours=models.CharField(max_length=255, null=True)
    )

    logo = models.ImageField(upload_to="uploads/logo/", null=True)
    phone_number = models.CharField(max_length=255)

    facebook_link = models.URLField(null=True)
    instagram_link = models.URLField(null=True)
    twitter_link = models.URLField(null=True)
    telegram_link = models.URLField(null=True)
    youtube_link = models.URLField(null=True)

    statistics_accepted = models.PositiveIntegerField(null=True)
    statistics_on_process = models.PositiveIntegerField(null=True)
    statistics_solved = models.PositiveIntegerField(null=True)
    statistics_not_solved = models.PositiveIntegerField(null=True)

    email_receiver = models.CharField(max_length=255, null=True)
    email_sender_address = models.EmailField(null=True)
    email_sender_password = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = _lazy("Site settings")
        verbose_name_plural = _lazy("Site settings")

    def __str__(self): return _("Site setting")


# Working
class Person(ViewCountMixin, OrderMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        full_name=models.CharField(max_length=255, null=True, blank=True),
        position=models.CharField(max_length=255),
        admission_days=models.CharField(max_length=255, null=True, blank=True),
        description=ckeditor_uploader_fields.RichTextUploadingField(null=True, blank=True),
        professional_history=ckeditor_uploader_fields.RichTextUploadingField(null=True, blank=True),
    )
    image = models.ImageField(upload_to="uploads/person/%Y/%m/%d/", null=True, blank=True)

    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    is_vacant = models.BooleanField(default=False)
    not_primary_staff = models.BooleanField(default=True)

    class Meta:
        verbose_name = _lazy("Person")
        verbose_name_plural = _lazy("Persons")

    def __str__(self): return self.safe_translation_getter('position', self.id)

    def clean(self):
        super().clean()

        if not self.is_vacant:
            non_vacant_required_fields = [
                'full_name',
                'position',
                'phone_number',
                'email',
            ]

            for field in non_vacant_required_fields:
                if not getattr(self, field, False):
                    raise django_core_exceptions.ValidationError({
                        field: _lazy("Required to fill field")
                    })
        else:
            non_vacant_required_fields = [
                'position',
            ]

            for field in non_vacant_required_fields:
                if not getattr(self, field, False):
                    raise django_core_exceptions.ValidationError({
                        field: _lazy("Required to fill field")
                    })

    def get_absolute_url(self): return urls.reverse('person_detail', args=[self.id])

    def resolve_image(self):
        return self.image.url if (self.image and (not self.is_vacant)) else static('../static/custom/img/person.jpg')


class Static(ViewCountMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255),
        content=ckeditor_uploader_fields.RichTextUploadingField(null=True, blank=True),
    )

    image = models.ImageField(upload_to='uploads/static/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        verbose_name = _lazy("Static page")
        verbose_name_plural = _lazy("Static pages")

    def clean(self):
        super().clean()
        if not self.title and not self.content:
            raise django_core_exceptions.ValidationError({
                'title': _lazy('Even one of title or content should have a value.'),
                'content': _lazy('Even one of title or content should have a value.'),
            })

    def __str__(self): return f"{ self.safe_translation_getter('title') if self.safe_translation_getter('title') else self.id }"


class PostCategory(OrderMixin, parler_models.TranslatableModel, mptt_models.MPTTModel, AddedUpdatedDateTimeMixin):
    parent = mptt_models.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255),
    )

    objects = managers.CustomMpttManager()

    class MPTTMeta:
        pass

    class Meta:
        verbose_name = _lazy("Post category")
        verbose_name_plural = _lazy("Post categories")

    def __str__(self): return f"{ self.safe_translation_getter('title', self.id) }"


class Post(ViewCountMixin, OrderMixin, parler_models.TranslatableModel, AddedUpdatedEditableDateTimeMixin):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255),
        short_description=models.CharField(max_length=1000, null=True),
        body=ckeditor_uploader_fields.RichTextUploadingField(),
    )

    post_category = models.ManyToManyField(PostCategory)

    image = models.ImageField(upload_to="uploads/post/%Y/%m/%d/")

    posting_date = models.DateTimeField(null=True, editable=True)

    class Meta:
        verbose_name = _lazy("Post")
        verbose_name_plural = _lazy("Posts")
        ordering = ['-posting_date']

    def __str__(self): return f"{ self.safe_translation_getter('title', self.id) }"

    @classmethod
    def published(self):
        return self.objects.filter(posting_date__lte=datetime.datetime.now(tz=pytz.timezone(timezone.get_current_timezone_name())))

    def get_absolute_url(self): return urls.reverse('post_detail', args=[self.id])


class PostImage(OrderMixin, AddedUpdatedDateTimeMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="uploads/post/%Y/%m/%d")

    class Meta:
        verbose_name = _lazy("Post image")
        verbose_name_plural = _lazy("Post images")

    def __str__(self): return f"{ self.post.safe_translation_getter('title', self.post.id) }"


class PostFile(OrderMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255, null=True, blank=True),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    file = models.FileField(upload_to="uploads/post_file/%Y/%m/")

    class Meta:
        verbose_name = _lazy("Post file")
        verbose_name_plural = _lazy("Post files")

    def __str__(self): return f"{ self.post.safe_translation_getter('title', self.post.id) } / { self.safe_translation_getter('title', self.id) }"


class OrganizationRegion(OrderMixin, parler_models.TranslatableModel, mptt_models.MPTTModel, AddedUpdatedDateTimeMixin):
    parent = mptt_models.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    translations = parler_models.TranslatedFields(
        name=models.CharField(max_length=255),
    )

    objects = managers.CustomMpttManager()

    class MPTTMeta:
        pass

    class Meta:
        verbose_name = _lazy("Organization region")
        verbose_name_plural = _lazy("Organization regions")

    def __str__(self): return f"{ self.safe_translation_getter('name', self.id) }"


class OrganizationCategory(OrderMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        name=models.CharField(max_length=255, null=True, blank=True),
    )

    display_regions_filter = models.BooleanField(default=False)

    class Meta(OrderMixin.Meta):
        verbose_name = _lazy("Organization category")
        verbose_name_plural = _lazy("Organization categories")

    def __str__(self): return f"{ self.safe_translation_getter('name', self.id) }"


class Organization(ViewCountMixin, OrderMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255, null=True),
        description=models.CharField(max_length=255, null=True),
        content=ckeditor_fields.RichTextField(blank=True, null=True),
        head_of_office=models.CharField(max_length=255, null=True),
        address=models.CharField(max_length=255, null=True),
    )
    organization_category = models.ForeignKey('OrganizationCategory', on_delete=models.CASCADE, null=True)
    region = models.ForeignKey('OrganizationRegion', on_delete=models.CASCADE, null=True)

    main_image = models.ImageField(upload_to='uploads/organization/%Y/%m/%d', null=True)
    location = geoposition_fields.GeopositionField(null=True)
    tel = models.CharField(max_length=255, null=True)
    website = models.URLField(null=True)

    class Meta:
        verbose_name = _lazy("Organization")
        verbose_name_plural = _lazy("Organizations")

    def __str__(self): return f"{ self.safe_translation_getter('title', self.id) }"

    def get_absolute_url(self): return urls.reverse('organization_detail', args=[self.id])

"""
main_aboutpagedata
main_aboutpagedata_translation
main_application
main_banner
main_banner_translation
main_event
main_event_translation
main_eventorder
main_keyindicator
main_keyindicator_translation
main_media
main_media_translation
main_mediaobject
main_menu
main_menu_translation
main_organization
main_organization_translation
main_organizationcategory
main_organizationcategory_translation
main_organizationregion
main_organizationregion_translation
main_person
main_person_translation
main_post
main_post_post_category
main_post_translation
main_postcategory
main_postcategory_translation
main_postfile
main_postfile_translation
main_postimage
main_regionaloffice
main_regionaloffice_translation
main_sitesettings
main_sitesettings_translation
main_static
main_static_translation
main_statisticaldata
main_typo
main_usefullink
main_usefullink_translation
poll_item
poll_item_translation
poll_poll
poll_poll_translation
poll_vote
"""


class AboutPageData(parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        address=models.CharField(max_length=500),
        destination=models.CharField(max_length=500),
        public_transport=models.CharField(max_length=500),
        work_days=models.CharField(max_length=255),
        work_hours=models.CharField(max_length=255),
    )

    phone_number = models.CharField(max_length=255, null=True)
    helpline = models.CharField(max_length=255, null=True)
    email1 = models.EmailField(max_length=255, null=True)
    email2 = models.EmailField(max_length=255, null=True)

    location_map_link = models.CharField(null=True, max_length=1000)

    class Meta:
        verbose_name = _lazy("About page data")
        verbose_name_plural = _lazy("About page data")

    def __str__(self): return _('About page data')


class RegionalOffice(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255),
        description=ckeditor_fields.RichTextField(),
        head_of_office=models.CharField(max_length=255),
        address=models.CharField(max_length=255),
    )
    logo = models.ImageField(upload_to="uploads/regional_office/")
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()

    name_in_english = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = _lazy("Regional office")
        verbose_name_plural = _lazy("Regional offices")

    def resolve_logo(self):
        return self.logo.url if self.logo else '/media/defaults/regional_office.png'

    def __str__(self): return self.safe_translation_getter('title', '-')


class Application(AddedUpdatedDateTimeMixin):
    LIST_APPLICATION_STATUS = (
        ('accepted', _lazy("Accepted")),
        ('reviewing', _lazy("Reviewing")),
        ('resolving', _lazy("Resolving")),
        ('rejected', _lazy("Rejected")),
    )

    region = models.CharField(max_length=255, choices=LIST_REGIONS, verbose_name=_lazy('Region'))
    full_name = models.CharField(max_length=255, verbose_name=_lazy('Full name'))
    email = models.EmailField(verbose_name=_lazy('E-Mail'))
    phone_number = models.CharField(max_length=255, verbose_name=_lazy('Phone number'))
    address = models.CharField(max_length=255, verbose_name=_lazy('Address'))
    file = models.FileField(upload_to="uploads/application/%Y/%m/%d", null=True, blank=True, verbose_name=_lazy('File'))
    content = ckeditor_fields.RichTextField(verbose_name=_lazy('Application content'))

    status = models.CharField(max_length=255, choices=LIST_APPLICATION_STATUS, default=LIST_APPLICATION_STATUS[0][0])

    class Meta:
        verbose_name = _lazy("Application")
        verbose_name_plural = _lazy("Applications")

    def __str__(self): return f"({ self.get_status_display() }) { self.time_added } @ { self.full_name }"


class Media(ViewCountMixin, OrderMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    LIST_MEDIA_TYPE = (
        ('video', _lazy('Video')),
        ('audio', _lazy('Audio')),
        ('photo', _lazy('Photo')),
    )

    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255),
        description=ckeditor_fields.RichTextField()
    )

    main_image = models.ImageField(upload_to="uploads/media/%Y/%m/%d")

    category = models.CharField(max_length=255, choices=LIST_MEDIA_TYPE, null=True)

    class Meta:
        verbose_name = _lazy("Media")
        verbose_name_plural = _lazy("Medias")

    def __str__(self): return f"{ self.safe_translation_getter('title', self.id) }"

    def get_absolute_url(self): return urls.reverse('media_gallery_detail', args=[self.id])


class MediaObject(models.Model):
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    # Photo gallery
    image = models.ImageField(upload_to="uploads/media/%Y/%m/%d", null=True, blank=True)

    # Video gallery
    video_file = models.FileField(
        upload_to="uploads/media/%Y/%m/%d",
        null=True,
        blank=True,
        validators=[
            django_core_validators.FileExtensionValidator(
                allowed_extensions=[
                    'mp4',
                    'avi',
                    'ogg',
                    'mkv',
                    'webm',
                ]
            )
        ]
    )

    youtube_video_id = models.CharField(max_length=255, null=True, blank=True)

    # Audio gallery
    audio_file = models.FileField(
        upload_to="uploads/media/%Y/%m/%d",
        null=True,
        blank=True,
        validators=[
            django_core_validators.FileExtensionValidator(
                allowed_extensions=[
                    'mp3',
                    'wav',
                    'aac',
                ]
            )
        ]
    )
    audio_link = models.URLField(null=True, blank=True)
    audio_artist = models.CharField(max_length=255, null=True, blank=True)
    audio_release_date = models.CharField(max_length=255, null=True, blank=True)
    audio_genre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _lazy("Media object")
        verbose_name_plural = _lazy("Media objects")

    def clean(self):
        if self.media.category == 'video':
            if self.video_file:
                pass
            elif self.youtube_video_id:
                pass
            else:
                return django_core_exceptions.ValidationError({
                    "video_file": _lazy("One of these field need to be filled"),
                    "youtube_video_id": _lazy("One of these field need to be filled"),
                })
        if self.media.category == 'audio':
            if self.audio_file:
                pass
            elif self.audio_link:
                pass
            else:
                return django_core_exceptions.ValidationError({
                    "audio_file": _lazy("One of these field need to be filled"),
                    "audio_link": _lazy("One of these field need to be filled"),
                })
        if self.media.category == 'photo':
            if self.image:
                pass
            else:
                return django_core_exceptions.ValidationError({
                    "image": _lazy("Image field must be filled"),
                })


class StatisticalData(AddedUpdatedDateTimeMixin):
    month = models.DateField(null=True)

    helpline_accepted = models.PositiveIntegerField(null=True)
    helpline_not_solved = models.PositiveIntegerField(null=True)
    helpline_on_process = models.PositiveIntegerField(null=True)
    helpline_solved = models.PositiveIntegerField(null=True)

    online_accepted = models.PositiveIntegerField(null=True)
    online_not_solved = models.PositiveIntegerField(null=True)
    online_on_process = models.PositiveIntegerField(null=True)
    online_solved = models.PositiveIntegerField(null=True)

    oral_accepted = models.PositiveIntegerField(null=True)
    oral_not_solved = models.PositiveIntegerField(null=True)
    oral_on_process = models.PositiveIntegerField(null=True)
    oral_solved = models.PositiveIntegerField(null=True)

    written_accepted = models.PositiveIntegerField(null=True)
    written_not_solved = models.PositiveIntegerField(null=True)
    written_on_process = models.PositiveIntegerField(null=True)
    written_solved = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = _lazy("Statistical data")
        verbose_name_plural = _lazy("Statistical datas")

    def __str__(self): return f"{ self.month.year } / { self.month.month }"


class Typo(models.Model):
    page = models.CharField(max_length=255)
    text = models.TextField()
    comment = models.TextField(null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _lazy("Typo")
        verbose_name_plural = _lazy("Typos")

    def __str__(self):
        return f'{ "Completed" if self.completed else "Not completed" } -- { self.date } -- { self.page }'


class UsefulLink(OrderMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255)
    )

    link = models.URLField(max_length=1000)
    image = models.ImageField(upload_to="uploads/useful_link/")

    class Meta(OrderMixin.Meta):
        verbose_name = _lazy("Useful link")
        verbose_name_plural = _lazy("Useful links")

    def __str__(self): return self.safe_translation_getter('title', str(self.id))


class KeyIndicator(OrderMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255)
    )

    icon = models.CharField(max_length=255, help_text=_lazy("Icons can be found from <a href='https://fontawesome.com/v5.15/icons'>here</a>"))
    value = models.PositiveIntegerField()

    class Meta(OrderMixin.Meta):
        verbose_name = _lazy("Key indicator")
        verbose_name_plural = _lazy("Key indicators")

    def __str__(self): return f"{ self.safe_translation_getter('title', self.id) }"


class Album(ViewCountMixin, parler_models.TranslatableModel, AddedUpdatedDateTimeMixin):
    LIST_FEST_OR_COMPETITION = (
        ('fest', _lazy("Festival")),
        ('competition', _lazy("Competition")),
    )
    LIST_LOCAL_OR_INTERNATIONAL = (
        ('local', _lazy("Local")),
        ('international', _lazy("International")),
    )

    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255),
        description=ckeditor_fields.RichTextField(null=True, blank=True),
        place=models.CharField(max_length=255, null=True, blank=True),
        organizer=ckeditor_fields.RichTextField(null=True, blank=True),
    )

    event_type = models.CharField(max_length=255, choices=LIST_FEST_OR_COMPETITION)
    region = models.CharField(max_length=255, choices=LIST_LOCAL_OR_INTERNATIONAL)

    class Meta:
        verbose_name = _lazy("Album")
        verbose_name_plural = _lazy("Albums")

    def __str__(self): return f"{ self.safe_translation_getter('title', self.id) }"

    def get_absolute_url(self): return urls.reverse('album_detail', args=[self.id])


class AlbumImage(parler_models.TranslatableModel):
    translations = parler_models.TranslatedFields(
        title=models.CharField(max_length=255, null=True, blank=True)
    )

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/album/%Y/%m/%d")

    def __str__(self): return f"{self.album.safe_translation_getter('title')}"



class Json(models.Model):
    name = models.CharField(max_length=50000)
    description = models.TextField()

    def __str__(self):
        return self.name