
from django.views import generic

from stripe_shop.models import Item


# Create your views here.
class ListItem(generic.ListView):
    """ Создание Item'a"""

    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Item.objects.all()
        return context


