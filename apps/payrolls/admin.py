from django.contrib import admin

from .models import Payroll


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ("actor","month", "status")
