from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel


class Leave(BaseModel):
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    report_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="leave_report_to"
    )
