import time

from .models import Payroll
from ..employees.models import Employee


def process_payrolls():
    print("Processing payrolls")
    employees = Employee.objects.all()

    for employee in employees:
        salary = employee.salary
        print(f"Processing payroll for employee {employee.full_name} with amount {employee.salary}")
        payroll = Payroll.objects.create(actor=employee.actor, amount=salary, status='pending')

        time.sleep(6)
        payroll.status = 'paid'
        payroll.save()

        time.sleep(6)
        print(f"Payroll for employee {employee.full_name} payed!")