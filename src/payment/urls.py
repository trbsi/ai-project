from django.urls import path

from . import views

urlpatterns = [
    path('my-subscriptions', views.my_subscriptions, name='my_subscriptions'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('payment-success', views.payment_success, name='payment_success_url'),
]
