from django.urls import path
from .views import EmployeeListView, EmployeeDetailView

urlpatterns = [
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path("employees/<str:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
]