from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee


def employee_form(request):

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        form = EmployeeForm()

    employees = Employee.objects.all()

    return render(
        request,
        'employee/employee_form.html',
        {
            'form': form,
            'employees': employees
        }
    )