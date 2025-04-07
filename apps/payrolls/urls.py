from django.urls import path
from .views import PayrollListView, PayrollProcessView

urlpatterns = [
    path("payroll/", PayrollListView.as_view(), name="payroll-list"),
    path("payroll/process/", PayrollProcessView.as_view(), name="payroll-process"),
]