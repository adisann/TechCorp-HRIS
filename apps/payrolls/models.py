from django.db import models

from core.models import BaseModel

PAYROLL_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('processing', 'Processing'),
    ('paid', 'Paid'),
)

class Payroll(BaseModel):
    month = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=100, choices=PAYROLL_STATUS_CHOICES, default='pending')
