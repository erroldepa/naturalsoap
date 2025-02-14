"""
URL configuration for naturalsoap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from naturalapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create-payment/', views.create_payment, name='create-payment'),
    path('execute-payment/', views.execute_payment, name='execute-payment'),
    path('cancel-payment/', views.cancel_payment, name='cancel-payment'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-cancel/', views.payment_cancel, name='payment-cancel'),
    path('payment-error/', views.payment_error, name='payment-error'),
    path('payment-failure/', views.payment_failure, name='payment-failure'),
]
