from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import urlencode


class CustomPasswordResetView(UserPassesTestMixin, PasswordResetView):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('home')

    def get_success_url(self):
        base_url = reverse('redirect_to')
        query_string = urlencode({'type': 'password_reset'})
        return f"{base_url}?{query_string}"
