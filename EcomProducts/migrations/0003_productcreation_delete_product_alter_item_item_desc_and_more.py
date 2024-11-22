# Generated by Django 5.1.2 on 2024-11-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EcomProducts", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductCreation",
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
                ("name", models.CharField(max_length=50)),
                ("product_ID", models.CharField(max_length=20)),
                ("description", models.TextField()),
                ("category", models.CharField(max_length=20)),
                ("location", models.CharField(default="World", max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("currency", models.CharField(default="USD", max_length=3)),
                ("image_url", models.URLField(blank=True, null=True)),
                (
                    "payment_interval",
                    models.CharField(
                        choices=[
                            ("one_time", "One Time"),
                            ("monthly", "Monthly"),
                            ("quaterly", "Quaterly"),
                            ("yearly", "Yearly"),
                        ],
                        default="one_time",
                        max_length=10,
                    ),
                ),
                ("quantity_available", models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name="Product",
        ),
        migrations.AlterField(
            model_name="item",
            name="item_desc",
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name="item",
            name="item_name",
            field=models.CharField(max_length=25),
        ),
    ]