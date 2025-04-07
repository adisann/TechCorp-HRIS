from django.contrib import admin

from .models import Leave


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ("actor__username", "start_date", "end_date", "is_approved")
    search_fields = ("actor__username",)
