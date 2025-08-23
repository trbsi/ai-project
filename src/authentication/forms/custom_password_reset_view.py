from django.contrib.auth.views import PasswordResetView
from django.urls import reverse
from django.utils.http import urlencode


class CustomPasswordResetView(PasswordResetView):
    def get_success_url(self):
        base_url = reverse('redirect_to')
        query_string = urlencode({'type': 'password_reset'})
        return f"{base_url}?{query_string}"
