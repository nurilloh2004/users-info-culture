import datetime

from . import models


def site_settings_context(request):
    now = datetime.date.today()

    return {
        "menus_in_header": models.Menu.objects.filter(display_in_main_menu=True, parent__isnull=True, translations__language_code=request.LANGUAGE_CODE),
        "menus_all": models.Menu.objects.filter(parent__isnull=True, translations__language_code=request.LANGUAGE_CODE),
        "site_settings": models.SiteSettings.objects.first(),
        "footer_upcoming_events": models.Event.objects.filter(start_date__date__gte=now, translations__language_code=request.LANGUAGE_CODE)[:3],
    }
