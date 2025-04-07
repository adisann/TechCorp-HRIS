from django.views.generic import ListView
from apps.employees.models import Employee
from core.views import LoginRequiredMixinView
from apps.employees.models import EmployeeSetting
from django.views.generic import DetailView
from apps.payrolls.models import Payroll  # Adjust this import based on your project structure

class EmployeeListView(LoginRequiredMixinView, ListView):
    model = Employee
    template_name = "employee_list.html"
    context_object_name = "employees"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_settings = EmployeeSetting.objects.get(actor=self.request.user)

        context["user_settings"] = user_settings
        return context

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.get_object()

        # Add annual salary
        context['annual_salary'] = (employee.salary or 0) * 12

        # Add payrolls
        if employee.actor:
            context['payrolls'] = Payroll.objects.filter(actor=employee.actor).order_by('-month')[:5]
        else:
            context['payrolls'] = Payroll.objects.none()

        return context
