from django.db import models

from core.models import BaseModel


class Announcement(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
