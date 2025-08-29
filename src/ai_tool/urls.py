from django.urls import path

from . import views

urlpatterns = [
    path('gpt', views.ai_tool, name='gpt_tool'),
    path('send-message', views.send_message, name='send_message'),
    path('poll-bot', views.poll_bot, name='poll_bot'),
]
