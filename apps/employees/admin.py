from django.contrib import admin

from .models import Employee, EmployeeSetting

@admin.register(EmployeeSetting)
class EmployeeSettingAdmin(admin.ModelAdmin):
    list_display = ('actor', 'role')
    list_filter = ('actor',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "job_title", "salary")
    search_fields = ("full_name",)
