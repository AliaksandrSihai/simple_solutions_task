from django import forms

from stripe_shop.models import Item


class ItemForm(forms.ModelForm):
    """Форма для модели Item"""

    class Meta:
        model = Item
        fields = "__all__"
