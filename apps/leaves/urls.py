from django.urls import path
from .views import LeavesListView, LeavesProcessView

urlpatterns = [
    path("leaves/", LeavesListView.as_view(), name="leaves-list"),
    path("leaves/process/", LeavesProcessView.as_view(), name="leaves-process"),
]