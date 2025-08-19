from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.http import require_GET, require_POST
from email_validator import validate_email, EmailNotValidError

@require_GET
def loginForm(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@require_POST
def login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'login.html', {'form': form})
