from django.contrib import admin
from .models import Product, Order
from .forms import ProductForm

admin.site.register(Product)
admin.site.register(Order)