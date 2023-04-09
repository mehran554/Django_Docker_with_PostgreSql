from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    # path('accounts/',include('accounts.urls')),
    path('', include('pages.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('payment/', include('payment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

