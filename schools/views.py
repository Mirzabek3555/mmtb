from django.shortcuts import render, get_object_or_404
from .models import School
from main.models import SiteSettings


def school_list(request):
    school_type = request.GET.get('type', '')
    qs = School.objects.filter(is_active=True)
    if school_type:
        qs = qs.filter(school_type=school_type)
    context = {
        'settings': SiteSettings.objects.first(),
        'schools': qs,
        'selected_type': school_type,
        'type_choices': School.TYPE_CHOICES,
        'total_students': sum(s.student_count for s in School.objects.filter(is_active=True)),
        'total_teachers': sum(s.teacher_count for s in School.objects.filter(is_active=True)),
    }
    return render(request, 'schools/list.html', context)


def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk, is_active=True)
    context = {
        'settings': SiteSettings.objects.first(),
        'school': school,
    }
    return render(request, 'schools/detail.html', context)
