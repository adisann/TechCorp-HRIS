from django.db import models
from core.models import BaseModel

class Ticket(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_solved = models.BooleanField(default=False)