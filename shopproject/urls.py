
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from . import settings

from django.conf.urls.static import static

urlpatterns = [
     path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
    path('admin/', admin.site.urls),
    path('',include('store.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
