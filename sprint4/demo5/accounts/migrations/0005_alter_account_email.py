# Generated by Django 4.1.6 on 2023-02-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_account_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
