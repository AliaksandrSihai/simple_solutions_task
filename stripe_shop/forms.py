from django import forms

from stripe_shop.models import Item, Order


class ItemForm(forms.ModelForm):
    """ Форма для модели Item """

    class Meta:
        model = Item
        fields = '__all__'


class OrderForm(forms.ModelForm):
    """ Форма для модели Order """

    class Meta:
        models = Order
        fields = '__all__'
