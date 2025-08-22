from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('user_settings')
    print(234234)
