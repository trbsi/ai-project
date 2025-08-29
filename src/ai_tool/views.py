from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def ai_tool(request: HttpRequest) -> HttpResponse:
    return render(request, 'gpt.html')
