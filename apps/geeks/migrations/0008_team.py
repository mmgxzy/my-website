# Generated by Django 5.1 on 2024-08-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geeks", "0007_index_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                (
                    "title",
                    models.CharField(
                        max_length=255,
                        verbose_name="Заголовок участника (на странице команда)",
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание участника ()")),
            ],
        ),
    ]