# Generated by Django 5.1 on 2024-08-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geeks", "0002_about_us"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="image2/", verbose_name="Фото")),
            ],
            options={
                "verbose_name_plural": "Фотография",
            },
        ),
    ]
