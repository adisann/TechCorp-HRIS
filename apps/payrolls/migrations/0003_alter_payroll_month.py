# Generated by Django 5.1.7 on 2025-03-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payrolls", "0002_remove_payroll_is_paid_payroll_amount_payroll_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payroll",
            name="month",
            field=models.DateField(auto_now_add=True),
        ),
    ]
