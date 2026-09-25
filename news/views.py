from django.shortcuts import render, get_object_or_404
from .models import News, NewsCategory
from main.models import SiteSettings


def news_list(request):
    category_slug = request.GET.get('category', '')
    qs = News.objects.filter(is_published=True)
    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(NewsCategory, slug=category_slug)
        qs = qs.filter(category=selected_category)
    context = {
        'settings': SiteSettings.objects.first(),
        'news_list': qs,
        'categories': NewsCategory.objects.all(),
        'selected_category': selected_category,
    }
    return render(request, 'news/list.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, is_published=True)
    news.views += 1
    news.save(update_fields=['views'])
    related = News.objects.filter(is_published=True).exclude(pk=news.pk)[:4]
    context = {
        'settings': SiteSettings.objects.first(),
        'news': news,
        'related_news': related,
    }
    return render(request, 'news/detail.html', context)
