# Generated by Django 4.1.7 on 2023-03-02 14:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="vehicle",
            old_name="amound_paid",
            new_name="amount_paid",
        ),
    ]