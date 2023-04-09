from django.contrib import admin
from .models import Order, OrderItem
from jalali_date.admin import ModelAdminJalaliMixin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price', ]
    extra = 1


class AdminOrder(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_create', 'is_paid', ]
    inlines = [OrderItemInline, ]


admin.site.register(Order, AdminOrder)


class AdminOrderItem(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', ]


admin.site.register(OrderItem, AdminOrderItem)
