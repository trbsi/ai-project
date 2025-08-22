from django.urls import path

from . import views

urlpatterns = [
    path('register', views.registrationForm, name='register'),
    path('do-register', views.register, name='do-register'),
]
