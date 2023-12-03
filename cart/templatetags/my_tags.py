from django import template

from cart.models import Order

register = template.Library()


@register.simple_tag
def total_amount(pk):
    model = Order.objects.get(pk=pk)
    amount = model.product.price * model.quantity
    return amount
