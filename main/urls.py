from django.urls import path
from django.contrib import admin
from django.utils.translation import gettext as _

from . import views

admin.site.site_header = _("Administration page of website madaniyat.uz")
admin.site.site_title = _("Administration page of website madaniyat.uz")
admin.site.index_title = _("Home page")


urlpatterns = [

    path('', views.HomeTemplate.as_view(), name='home_template_view'),

    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:id>', views.PostDetail.as_view(), name='post_detail'),

    path('static/<int:id>', views.StaticDetail.as_view(), name='static_detail'),
    path('json/', views.formatJson, name='json'),

    path('application', views.ApplicationForm.as_view(), name='application_form'),
    path('contact', views.ContactPage.as_view(), name='contact_view'),

    path('person/', views.PersonList.as_view(), name='person_list'),
    path('person/<int:id>', views.PersonDetail.as_view(), name='person_detail'),

    path('regions/', views.RegionsList.as_view(), name="regions-list"),

    path('organization/', views.OrganizationList.as_view(), name='organization_list'),
    path('organization/<int:id>', views.OrganizationDetail.as_view(), name='organization_detail'),

    path('event/', views.EventList.as_view(), name='event_list'),
    path('event/<int:id>', views.EventDetail.as_view(), name='event_detail'),

    path('media/', views.MediaTemplate.as_view(), name='media_list'),

    path('media/items/', views.MediaGalleryList.as_view(), name='media_gallery_list'),
    path('media/items/<int:id>', views.MediaGalleryDetail.as_view(), name='media_gallery_detail'),

    path('statistics/', views.StatisticsList.as_view(), name='statistics_template'),
    path('search/', views.SearchTemplateView.as_view(), name='search_template'),

    path('album/', views.AlbumList.as_view(), name='album_list'),
    path('album/<int:id>', views.AlbumDetail.as_view(), name='album_detail'),

]

urlpatterns += [
    path('api/typo-report', views.TypoReportAPI.as_view(), name='typo_report_api'),
]
