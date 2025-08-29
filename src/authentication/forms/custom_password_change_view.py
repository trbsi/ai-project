from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('user_settings')

    def get_success_url(self):
        base_url = reverse_lazy('redirect_to')
        return f"{base_url}?type=password_change"
