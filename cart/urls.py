from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('clera/', views.cart_clear, name='cart_clear'),
    path('add/<int:product_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('del/<int:product_id>/', views.del_from_cart, name='del_from_cart'),
    # path('', views.cart_detail_view, name='cart_detail'),

]
