from django.shortcuts import redirect
from django.views import generic, View
from django.views.generic import TemplateView
from cart.models import Order
from cart.service import create_payment


class SuccessTemplateView(TemplateView):
    template_name = "cart/success_order.html"
    title = " Спасибо за заказ!"


class OrderTemplateView(TemplateView):
    template_name = "cart/order_form.html"


class CanceledTemplateView(TemplateView):
    template_name = "cart/canceled.html"


class OrdersListView(generic.ListView):
    """Просмотр заказов"""

    model = Order

    template_name = "cart/order_form.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Order.objects.select_related("product").filter(
            user=self.request.user, status=False
        )
        if cart.exists():
            context["object_list"] = cart
        return context


class CreateStripe(View):
    """Создание платежа в Stripe"""

    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        price = order.product.price * order.quantity

        if order.discount is not None:
            discount = price * order.discount.percent / 100
            price -= discount

        if order.tax is not None:
            tax = price * order.tax.tax_percent / 100
            price += tax
        try:
            stripe_id = create_payment(
                amount=price, currency=order.product.currency.lower()
            )
            order.stripe_id = stripe_id
            order.status = True
            order.save()
            return redirect("cart:order_success")
        except ValueError:
            return redirect("cart:order_cancel")
