from django.urls import path

from . import views

urlpatterns = [
    path('login', views.loginForm, name='login'),
    path('do-login', views.login, name='do-login'),
    path('register', views.registrationForm, name='register'),
    path('do-register', views.register, name='do-register'),
    path('forgot-password', views.forgotPasswordForm, name='forgot-password'),
    path('do-forgot-password', views.forgotPassword, name='do-forgot-password'),
]
