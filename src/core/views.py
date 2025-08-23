from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def home(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('user_settings')
    else:
        return redirect('login')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def redirect_to(request: HttpRequest) -> HttpResponse:
    type = request.GET.get('type')

    if type == 'password_reset':
        messages.success(request, 'Password reset link has been sent to your email')
        return redirect('login')

    return redirect('home')
