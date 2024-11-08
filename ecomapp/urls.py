from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.home_views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', index, name='home'),
    path('addproduct', add_product, name = 'add_product'),
    path('products', products, name='products'),
    path('checkout/<int:id>', checkout, name='checkout'),
    path('cartitems', cartitems, name='cartitems'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
