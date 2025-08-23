from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('redirect-to', views.redirect_to, name='redirect_to'),
]
