from django.contrib import admin
from django.utils.translation import gettext as _

from adminsortable2 import admin as adminsortable2_admin
from mptt import admin as mptt_admin
from parler import admin as parler_admin

from project import settings

from . import models


class PaginationMixin:
    list_per_page = 30


@admin.register(models.Person)
class PersonAdmin(PaginationMixin, parler_admin.TranslatableAdmin, adminsortable2_admin.SortableAdminMixin):
    list_display = [
        'full_name',
        'view_count',
        'position',
        'admission_days',
        'is_vacant',
        'not_primary_staff',
        'time_added',
        'time_updated',
    ]


@admin.register(models.Banner)
class BannerAdmin(PaginationMixin, adminsortable2_admin.SortableAdminMixin, parler_admin.TranslatableAdmin):
    pass


@admin.register(models.EventOrder)
class EventOrderAdmin(PaginationMixin, admin.ModelAdmin):
    pass


@admin.register(models.Typo)
class TypoAdmin(PaginationMixin, admin.ModelAdmin):
    pass


@admin.register(models.UsefulLink)
class UsefulLinkAdmin(adminsortable2_admin.SortableAdminMixin, PaginationMixin, parler_admin.TranslatableAdmin):
    pass


@admin.register(models.KeyIndicator)
class KeyIndicatorAdmin(adminsortable2_admin.SortableAdminMixin, PaginationMixin, parler_admin.TranslatableAdmin):
    pass


@admin.register(models.Static)
class StaticAdmin(PaginationMixin, parler_admin.TranslatableAdmin):
    list_display = [
        'title',
        'view_count',
        'time_added',
        'time_updated',
    ]


@admin.register(models.Event)
class EventAdmin(PaginationMixin, parler_admin.TranslatableAdmin):
    list_display = [
        'title',
        'view_count',
        'event_type',
        'address',
        'organizer',
        'price',
        'start_date',
        'end_date',
        'time_added',
        'time_updated',
    ]
    list_editable = [
        'start_date',
        'end_date',
    ]


@admin.register(models.PostCategory)
class PostCategoryAdmin(PaginationMixin, parler_admin.TranslatableAdmin, mptt_admin.DraggableMPTTAdmin):
    pass


@admin.register(models.AboutPageData)
class AboutPageDataAdmin(PaginationMixin, parler_admin.TranslatableAdmin):
    def has_add_permission(self, request): return False
    def has_delete_permission(self, request, obj=None): return False


@admin.register(models.RegionalOffice)
class RegionalOfficeAdmin(PaginationMixin, parler_admin.TranslatableAdmin):
    pass


@admin.register(models.OrganizationCategory)
class OrganizationCategoryAdmin(adminsortable2_admin.SortableAdminMixin, PaginationMixin, parler_admin.TranslatableAdmin):
    pass


@admin.register(models.OrganizationRegion)
class OrganizationRegionAdmin(parler_admin.TranslatableAdmin, mptt_admin.DraggableMPTTAdmin):
    pass


@admin.register(models.Organization)
class OrganizationAdmin(PaginationMixin, parler_admin.TranslatableAdmin):
    list_display = [
        'title',
        'view_count',
        'head_of_office',
        'region',
        'address',
        'organization_category',
        'tel',
        'website',
        'time_added',
        'time_updated',
    ]


@admin.register(models.Application)
class ApplicationAdmin(PaginationMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'full_name',
        'region',
        'email',
        'phone_number',
        'address',
        'status',
        'time_added',
        'time_updated',
    ]


@admin.register(models.StatisticalData)
class StatisticalDataAdmin(PaginationMixin, admin.ModelAdmin):
    # form = forms.StatisticalDataAdminForm
    list_display = [
        'custom_month',
        'helpline_accepted',
        'helpline_not_solved',
        'helpline_on_process',
        'helpline_solved',
        'online_accepted',
        'online_not_solved',
        'online_on_process',
        'online_solved',
        'oral_accepted',
        'oral_not_solved',
        'oral_on_process',
        'oral_solved',
        'written_accepted',
        'written_not_solved',
        'written_on_process',
        'written_solved',
    ]

    def custom_month(self, obj):
        return obj.month.strftime('%b / %Y')

    custom_month.admin_order_field = 'month'
    custom_month.short_description = _('Month')


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(PaginationMixin, parler_admin.TranslatableAdmin):
    def has_add_permission(self, request): return True
    def has_delete_permission(self, request, obj=None): return False


@admin.register(models.Menu)
class MenuAdmin(parler_admin.TranslatableAdmin, mptt_admin.DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title'
    )
    list_display_links = (
        'indented_title',
    )
    mptt_level_indent = 20

    def get_available_languages(self, obj):
        return [LANGUAGE[0] for LANGUAGE in settings.LANGUAGES]


class MediaObjectAdmin(PaginationMixin, admin.StackedInline):
    model = models.MediaObject


@admin.register(models.Media)
class MediaAdmin(PaginationMixin, parler_admin.TranslatableAdmin):
    list_display = [
        'title',
        'category',
    ]
    inlines = [
        MediaObjectAdmin
    ]


class PostFileInline(parler_admin.TranslatableTabularInline):
    model = models.PostFile


class PostImageInline(admin.TabularInline):
    model = models.PostImage


@admin.register(models.Post)
class PostAdmin(PaginationMixin, parler_admin.TranslatableAdmin):
    list_display = [
        'posting_date',
        'title',
        'view_count',
        'posting_date',
        'short_description',
        'time_added',
        'time_updated',
    ]
    # list_editable = [
    #     'title',
    # ]
    inlines = [
        PostFileInline,
        PostImageInline
    ]


class AlbumImageAdmin(PaginationMixin, parler_admin.TranslatableTabularInline):
    model = models.AlbumImage


@admin.register(models.Album)
class AlbumAdmin(PaginationMixin, parler_admin.TranslatableAdmin):
    list_display = [
        'title',
        'place',
        'event_type',
        'region',
        'time_added',
        'time_updated',
    ]
    inlines = [
        AlbumImageAdmin
    ]
