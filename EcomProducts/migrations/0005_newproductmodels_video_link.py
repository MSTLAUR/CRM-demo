# Generated by Django 5.1.2 on 2024-11-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EcomProducts", "0004_newproductmodels_delete_productcreation"),
    ]

    operations = [
        migrations.AddField(
            model_name="newproductmodels",
            name="video_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]