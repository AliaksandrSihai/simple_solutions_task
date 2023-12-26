from api.apps import ApiConfig
from rest_framework import routers
from django.urls import path
from api.views import ItemViewSet, CartRetrieveAPIView

app_name = ApiConfig.name


router = routers.DefaultRouter()
router.register(r"item", ItemViewSet, basename="item")


urlpatterns = [
    path("cart/<int:pk>/", CartRetrieveAPIView.as_view(), name="cart"),
] + router.urls
