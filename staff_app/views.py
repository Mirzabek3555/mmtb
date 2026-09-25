from django.shortcuts import render
from .models import Staff, Department
from main.models import SiteSettings


def staff_list(request):
    dept_id = request.GET.get('department', '')
    management = Staff.objects.filter(is_management=True)
    staff_qs = Staff.objects.filter(is_management=False)
    if dept_id:
        staff_qs = staff_qs.filter(department_id=dept_id)
    context = {
        'settings': SiteSettings.objects.first(),
        'management': management,
        'staff': staff_qs,
        'departments': Department.objects.all(),
        'selected_dept': dept_id,
    }
    return render(request, 'staff_app/staff.html', context)
