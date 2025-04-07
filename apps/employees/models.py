from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel

ROLE_CHOICES = (
    ('user', 'User'),
    ('manager', 'Manager'),
)

class EmployeeSetting(BaseModel):
    actor = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=120, choices=ROLE_CHOICES, default='user')

class Employee(BaseModel):
    actor = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.DateField()
    date_of_birth = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
