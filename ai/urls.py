"""
URL configuration for ai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

from src.authentication.forms.custom_password_change_view import CustomPasswordChangeView
from src.authentication.forms.custom_password_reset_view import CustomPasswordResetView

urlpatterns = [
    # core
    path('', include('src.core.urls')),

    # admin
    path('admin/', admin.site.urls),

    # user
    path('user/', include('src.user.urls')),

    # auth
    path('auth/password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('auth/password_reset/', CustomPasswordResetView.as_view(), name='password-reset'),
    path('auth/', include('django.contrib.auth.urls')),
    path('authentication/', include('src.authentication.urls')),
]
