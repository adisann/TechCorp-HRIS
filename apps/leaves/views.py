from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from apps.leaves.models import Leaves
from apps.employees.models import Employee, EmployeeSetting
from apps.leaves.tasks import process_leaves_task
from core.views import LoginRequiredMixinView


class LeavesListView(LoginRequiredMixinView, ListView):
    model = Leaves
    template_name = "leaves_list.html"
    context_object_name = "leaves"

    def get_queryset(self):
        return Leaves.objects.filter(actor=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        employee = Employee.objects.filter(actor=self.request.user).first()
        user_settings = EmployeeSetting.objects.get(actor=self.request.user)

        context['employee'] = employee
        context['user_settings'] = user_settings

        return context

class LeavesProcessView(LoginRequiredMixinView, View):
    def get(self, request):
        user_settings = EmployeeSetting.objects.get(actor=request.user)
        return render(request, 'leaves_process.html', {'user_settings': user_settings})

    def post(self, request):
        action = request.POST.get('action')

        if action == 'process':
            process_leaves_task()

        return redirect('payroll-process')