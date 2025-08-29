from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def home(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('gpt_tool')
    else:
        return redirect('login')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def redirect_to(request: HttpRequest) -> HttpResponse:
    type = request.GET.get('type')

    if type == 'password_reset':
        messages.success(request, 'Password reset link has been sent to your email')
        return redirect('login')

    if type == 'password_change':
        messages.success(request, 'Password has been reset')
        return redirect('password_change')

    if type == 'payment_success':
        messages.success(request, 'Subscription is active')
        return redirect('my_subscriptions')

    if type == 'forbidden_by_subscription':
        messages.error(request, 'You have to subscribe in order to access this page')
        return redirect('my_subscriptions')

    return redirect('home')
