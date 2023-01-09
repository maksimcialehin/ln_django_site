from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from apps_site import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('business_apps.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
