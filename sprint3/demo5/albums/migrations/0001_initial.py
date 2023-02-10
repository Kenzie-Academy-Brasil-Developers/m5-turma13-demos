# Generated by Django 4.1.6 on 2023-02-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=127)),
                ("year", models.PositiveSmallIntegerField()),
                ("serial_number", models.IntegerField(unique=True)),
            ],
        ),
    ]
