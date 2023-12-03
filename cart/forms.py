from django.forms import ModelForm

from cart.models import Order


class CartForm(ModelForm):
    """ Форма для корзины """
    class Meta:
        model = Order
        fields = '__all__'
