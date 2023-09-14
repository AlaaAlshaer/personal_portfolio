# Generated by Django 4.2.4 on 2023-09-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=50)),
                ("descrption", models.TextField()),
                ("tecnologe", models.CharField(max_length=20)),
                ("image", models.FilePathField(path="/img")),
            ],
        ),
    ]
