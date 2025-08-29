from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


@require_POST
@login_required
def settings(request: HttpRequest) -> HttpResponse:
    return render(request, 'user_settings.html')
