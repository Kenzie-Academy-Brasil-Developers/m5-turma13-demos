# Generated by Django 4.1.6 on 2023-02-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("albums", "0003_alter_album_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="name",
            field=models.CharField(db_column="nome", max_length=127),
        ),
    ]
