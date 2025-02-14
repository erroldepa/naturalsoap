from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
import os
from .models import Product, Order
from .forms import ProductForm
from django.contrib import messages
import requests
import pickle as pk
from django.urls import path

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
def create_payment(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        product = Product.objects.get(id=product_id)
        total = product.price * quantity
        return JsonResponse({'total': total})
    return render(request, 'index.html')
def execute_payment(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        product = Product.objects.get(id=product_id)
        total = product.price * quantity
        order = Order.objects.create(product=product, quantity=quantity, total=total)
        order.save()
        messages.success(request, 'Payment successful!')
        return redirect('payment-success')
    return render(request, 'index.html')

def cancel_payment(request):
    return render(request, 'cancel.html')

def payment_success(request):
    return render(request, 'success.html')

def payment_cancel(request):
    return render(request, 'cancel.html')

def payment_error(request):
    return render(request, 'error.html')

def payment_failure(request):
    return render(request, 'failure.html')

def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('index')
    return render(request, 'create_product.html', {'form': form})

def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('index')
    return render(request, 'update_product.html', {'form': form})

def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('index')

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})
def view_order(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'order.html', {'order': order})  # Render the order.html template with the order object
