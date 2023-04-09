from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_register_view, name='order_register'),

]
