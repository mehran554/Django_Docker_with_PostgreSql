from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext as _
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(_('Name'), max_length=100)
    last_name = models.CharField(_('Family'), max_length=100)
    phone_number = models.CharField(_('PhoneNumber'), max_length=15)
    address = models.CharField(_('Address'), max_length=700)
    order_note = models.CharField(_('Order_Note'), max_length=700, blank=True)
    zarinpal_authority = models.CharField(max_length=256, blank=True)
    datetime_create = models.DateTimeField(_('Created Time'), default=timezone.now)
    datetime_modified = models.DateTimeField(_('Modified Time'), auto_now=True)
    is_paid = models.BooleanField(_('Is_Paid?'), default=False)

    def get_total_price(self):
        result = 0
        for item in self.items.all():
            result += item.quantity * item.price
        return result

    def __str__(self):
        return f'order:{self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f' Order No: {self.order} Contains->Product:{self.product} x qty:{self.quantity} (price:{self.price})'
