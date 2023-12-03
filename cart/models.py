from django.db import models

from stripe_shop.models import Item
from users.models import NULLABLE


# Create your models here.
class Order(models.Model):
    """ Модель для корзины """

    product = models.ForeignKey(to=Item, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    discount = models.ForeignKey(to='Discount', on_delete=models.CASCADE, related_name='discounts', **NULLABLE)
    tax = models.ForeignKey(to='Tax', on_delete=models.CASCADE, related_name='tax', **NULLABLE)
    stripe_id = models.CharField(max_length=40, verbose_name='id платежа на stripe', **NULLABLE)
    status = models.BooleanField(default=False, verbose_name='статус платежа')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class Discount(models.Model):
    """ Модель для скидки"""

    percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.percent

    class Meta:
        verbose_name = 'скидка'
        verbose_name_plural = 'скидки'


class Tax(models.Model):
    """ Модель для налога """

    tax_name = models.TextField(**NULLABLE, verbose_name='наименование налога')
    tax_percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.tax_name

    class Meta:
        verbose_name = 'налог'
        verbose_name_plural = 'налоги'
