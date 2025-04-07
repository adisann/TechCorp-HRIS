from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "is_solved")
    search_fields = ("title",)
    list_filter = ("is_solved",)