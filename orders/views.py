from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrdersRegisterForm
from cart.cart import Cart
from .models import Order, OrderItem


def order_register_view(request):
    form = OrdersRegisterForm()
    cart = Cart(request)
    if request.method == 'POST':
        form = OrdersRegisterForm(request.POST)
        if form.is_valid():
            order_obj = form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()
            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,

                )

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()
            cart.clear()
            # messages.success(request, "سفارش شما با موفقیت ثبت شد ")
            request.session['order_id'] = order_obj.id
            return redirect('payment:payment_process')
    return render(request, 'order/order_view.html', {'form': form})
