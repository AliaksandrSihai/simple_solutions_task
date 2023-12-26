from stripe_shop.apps import StripeShopConfig
from django.urls import path

from stripe_shop.views import ListItem, RetrieveItem, BuyItemView

app_name = StripeShopConfig.name

urlpatterns = [
    path("", ListItem.as_view(), name="items"),
    path("item/<int:pk>", RetrieveItem.as_view(), name="item_details"),
    path("buy/<int:pk>", BuyItemView.as_view(), name="buy_item"),
]
