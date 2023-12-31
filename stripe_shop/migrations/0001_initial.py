# Generated by Django 4.2.7 on 2023-12-01 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Discount",
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
                ("percent", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name": "скидка",
                "verbose_name_plural": "скидки",
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=255, verbose_name="название")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="описание"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="цена"
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[("USD", "USD"), ("RUB", "RUB")],
                        max_length=3,
                        verbose_name="валюта",
                    ),
                ),
            ],
            options={
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
            },
        ),
        migrations.CreateModel(
            name="Tax",
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
                    "tax_name",
                    models.TextField(
                        blank=True, null=True, verbose_name="наименование налога"
                    ),
                ),
                ("tax_percent", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name": "налог",
                "verbose_name_plural": "налоги",
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                    "quantity",
                    models.PositiveIntegerField(default=0, verbose_name="количество"),
                ),
                (
                    "stripe_id",
                    models.CharField(
                        blank=True,
                        max_length=40,
                        null=True,
                        verbose_name="id платежа на stripe",
                    ),
                ),
                (
                    "status",
                    models.BooleanField(default=False, verbose_name="статус платежа"),
                ),
                ("order_date", models.DateTimeField(auto_now_add=True)),
                (
                    "discount",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="discounts",
                        to="stripe_shop.discount",
                    ),
                ),
                ("product", models.ManyToManyField(to="stripe_shop.item")),
                (
                    "tax",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tax",
                        to="stripe_shop.tax",
                    ),
                ),
            ],
            options={
                "verbose_name": "заказ",
                "verbose_name_plural": "заказы",
            },
        ),
    ]
