from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import resolve, reverse_lazy
from django.utils.http import urlencode

from src.payment.models import Subscription


class SubscriptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        current_url = resolve(request.path_info).url_name
        forbidden_urls = ['gpt_tool']

        if current_url in forbidden_urls:
            user: User = request.user
            user_subscription: Subscription = Subscription.objects.filter(user=user).first()
            if user_subscription is None or user_subscription.is_active() == False:
                url = reverse_lazy('redirect_to')
                query = urlencode({'type': 'forbidden_by_subscription'})
                return redirect(f"{url}?{query}")

        return self.get_response(request)
