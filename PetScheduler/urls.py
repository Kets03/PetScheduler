from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from care.views import get_started

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_started, name='get_started'),
    path('care/', include('care.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)