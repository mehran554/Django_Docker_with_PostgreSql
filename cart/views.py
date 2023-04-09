from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .cart import Cart
from django.utils.translation import gettext as _
from products.models import Product
from django.contrib import messages
# from django.contrib.
from .forms import AddToCartForm


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_qty_set'] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart/cart_detail.html', {'cart': cart})
    # return render(request, 'cart/cart_detail.html')


def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        product_qty_add = cleaned_data['inplace']
        cart.add(product, quantity, product_qty_add)
        messages.success(request, _('Product Successfully Added To Cart'))
    return redirect('product_list')
    # return redirect('product_list')23


def del_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    cart.save()
    messages.error(request, _('Product Successfully Deleted From Cart'))
    return redirect('cart:cart_detail')


def cart_clear(request):
    cart = Cart(request)
    if cart:
        cart.clear()
        messages.success(request, _("Your Cart Successfully clear "))
    else:
        messages.error(request, _("Your Cart Is Already Clear!!!!!"))

    return redirect('product_list')
