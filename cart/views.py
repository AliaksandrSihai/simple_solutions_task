from django.shortcuts import redirect
from django.views import generic, View
from django.views.generic import TemplateView
from cart.models import Order
from cart.service import create_payment


class SuccessTemplateView(TemplateView):
    template_name = 'cart/success_order.html'
    title = ' Спасибо за заказ!'


class OrderTemplateView(TemplateView):
    template_name = 'cart/order_form.html'


class CanceledTemplateView(TemplateView):
    template_name = 'cart/canceled.html'


class OrdersListView(generic.ListView):
    """ Просмотр заказов """

    model = Order

    template_name = 'cart/order_form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Order.objects.select_related('product').filter(status=False)
        return context


class CreateStripe(View):
    """ Создание платежа в Stripe"""
    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        try:
            order.stripe_id = create_payment(quantity=order.quantity, amount=order.product.price,
                                             currency=order.product.currency.lower())
            order.save()
            return redirect('cart:order_success')
        except ValueError:
            return redirect('cart:order_cancel')
