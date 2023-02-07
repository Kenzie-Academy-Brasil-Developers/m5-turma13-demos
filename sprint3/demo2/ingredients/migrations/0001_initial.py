# Generated by Django 4.1.6 on 2023-02-06 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
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
                ("name", models.CharField(max_length=40)),
                (
                    "recipes",
                    models.ManyToManyField(
                        related_name="ingredients", to="recipes.recipe"
                    ),
                ),
            ],
        ),
    ]
