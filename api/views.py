from rest_framework import viewsets, generics
from cart.models import Order
from cart.serializers import CartSerializer
from stripe_shop.models import Item
from stripe_shop.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """Вьюсет для товара"""

    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class CartRetrieveAPIView(generics.RetrieveAPIView):
    """Вьюсет для корзины"""

    serializer_class = CartSerializer
    queryset = Order.objects.all()
