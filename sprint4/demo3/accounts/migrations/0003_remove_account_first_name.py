# Generated by Django 4.1.6 on 2023-02-13 12:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_account_birthdate_account_cpf"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="first_name",
        ),
    ]