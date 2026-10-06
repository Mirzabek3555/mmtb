from django.shortcuts import render, get_object_or_404
from news.models import News
from main.models import Statistics, Announcement, Document, SiteSettings
from schools.models import School
from staff_app.models import Staff


def get_settings():
    return SiteSettings.objects.first()


def index(request):
    context = {
        'settings': get_settings(),
        'featured_news': News.objects.filter(is_published=True, is_featured=True)[:3],
        'latest_news': News.objects.filter(is_published=True)[:6],
        'statistics': Statistics.objects.all(),
        'announcements': Announcement.objects.filter(is_active=True)[:5],
        'schools_count': School.objects.filter(is_active=True).count(),
        'management': Staff.objects.filter(is_management=True)[:4],
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'settings': get_settings(),
        'management': Staff.objects.filter(is_management=True),
        'statistics': Statistics.objects.all(),
    }
    return render(request, 'main/about.html', context)


def documents(request):
    category = request.GET.get('category', '')
    qs = Document.objects.all()
    if category:
        qs = qs.filter(category=category)
    context = {
        'settings': get_settings(),
        'documents': qs,
        'selected_category': category,
        'categories': Document.CATEGORY_CHOICES,
    }
    return render(request, 'main/documents.html', context)


def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk, is_active=True)
    context = {
        'settings': get_settings(),
        'announcement': announcement,
    }
    return render(request, 'main/announcement_detail.html', context)
