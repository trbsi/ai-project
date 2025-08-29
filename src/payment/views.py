from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.decorators.http import require_GET, require_POST

from src.payment.models import Subscription
from .services import SubscribeService


@require_GET
@login_required
def my_subscriptions(request: HttpRequest) -> HttpResponse:
    user = request.user
    payment = Subscription.objects.filter(user=user).first()
    return render(request, 'my_subscriptions.html', {'payment': payment})


@require_POST
@login_required
def subscribe(request: HttpRequest, subscribe_service: SubscribeService):
    user: User = request.user
    package: str = request.POST.get('package')
    url: str = subscribe_service.subscribe(user, package)
    return redirect(url)


@require_GET
@login_required
def payment_success(request: HttpRequest, subscribe_service: SubscribeService) -> HttpResponse:
    user: User = request.user
    subscribe_service.activate_subscription(user)

    url = reverse_lazy('redirect_to')
    params = urlencode({'type': 'payment_success'})
    return redirect(f"{url}?{params}")
