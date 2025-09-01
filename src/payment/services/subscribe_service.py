import datetime

from django.contrib.auth.models import User
from django.urls import reverse_lazy

from src.payment.models import Subscription, Package
from . import StripeService


class SubscribeService:
    def subscribe(self, user: User, package: str) -> str:
        subscription: Subscription = Subscription.objects.filter(user=user).first()

        if subscription is None:
            subscription = Subscription.objects.create(user=user, package=package)

        subscription.active_until = None
        subscription.save()

        package: Package = Package.objects.filter(name=package).first()

        return reverse_lazy('payment_success_url')
        # TODO implement Stripe
        stripe_service: StripeService = StripeService()
        return stripe_service.create_checkout_session(package.price, package.name)

    def activate_subscription(self, user: User) -> None:
        subscription: Subscription = Subscription.objects.filter(user=user).first()
        subscription.active_until = datetime.datetime.now() + datetime.timedelta(days=30)
        subscription.save()
