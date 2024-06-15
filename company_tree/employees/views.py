from django.shortcuts import render
from .models import Department

def department_tree(request):
    departments = Department.objects.filter(parent__isnull=True).prefetch_related('children__children__children__children__children')
    return render(request, 'employees/department_tree.html', {'departments': departments})
