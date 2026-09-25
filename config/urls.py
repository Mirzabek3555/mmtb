from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('main.urls')),
    path('yangiliklar/', include('news.urls')),
    path('maktablar/', include('schools.urls')),
    path('galereya/', include('gallery.urls')),
    path('xodimlar/', include('staff_app.urls')),
    path('murojaat/', include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
