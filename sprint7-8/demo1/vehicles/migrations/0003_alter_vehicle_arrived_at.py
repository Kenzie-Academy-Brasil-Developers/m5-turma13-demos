# Generated by Django 4.1.7 on 2023-03-06 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0002_rename_amound_paid_vehicle_amount_paid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="arrived_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
