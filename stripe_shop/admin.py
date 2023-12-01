from django.contrib import admin

from stripe_shop.models import Item, Order, Discount, Tax

# Register your models here.
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Discount)
admin.site.register(Tax)
