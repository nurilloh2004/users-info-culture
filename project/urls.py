from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

from main import views as main_views


handler404 = main_views.NotFoundTemplateView.as_view()

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include("poll.urls", namespace='poll')),
    prefix_default_language=True
)

urlpatterns += [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += [
    path('rosetta/', include('rosetta.urls')),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

