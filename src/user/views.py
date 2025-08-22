from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def settings(request: HttpRequest) -> HttpResponse:
    return render(request, 'user_settings.html')