from django.urls import path
from .views import AnnouncementListView, DefaultView

urlpatterns = [
    path("dashboard/", AnnouncementListView.as_view(), name="announcement-list"),
    path("", DefaultView.as_view(), name="index"),
]