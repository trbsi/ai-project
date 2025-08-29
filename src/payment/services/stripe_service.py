import stripe
from django.conf import settings
from django.urls import reverse_lazy


class StripeService:
    def create_checkout_session(self, price: float, package_name: str) -> str:
        stripe.api_key = settings.env('STRIPE_SECRET_KEY')
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': package_name,
                            },
                            'unit_amount': price * 100
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=reverse_lazy('payment_success_url'),
                cancel_url=reverse_lazy('my_subscriptions'),
            )
        except Exception as e:
            return str(e)

        return checkout_session.url
