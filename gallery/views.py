from django.shortcuts import render
from .models import GalleryImage, GalleryCategory, Video
from main.models import SiteSettings


def gallery(request):
    category_id = request.GET.get('category', '')
    images_qs = GalleryImage.objects.filter(is_active=True)
    if category_id:
        images_qs = images_qs.filter(category_id=category_id)
    context = {
        'settings': SiteSettings.objects.first(),
        'images': images_qs,
        'categories': GalleryCategory.objects.all(),
        'selected_category': category_id,
        'videos': Video.objects.filter(is_active=True)[:6],
    }
    return render(request, 'gallery/gallery.html', context)
