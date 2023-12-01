from stripe_shop.apps import StripeShopConfig
from django.urls import path

from stripe_shop.views import ListItem

app_name = StripeShopConfig.name

urlpatterns = [
    path('', ListItem.as_view(), name='items')
]