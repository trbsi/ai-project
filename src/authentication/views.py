from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST

from src.authentication.forms.custom_user_creation_form import CustomUserCreationForm


@require_GET
def registrationForm(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('home')
    form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})


@require_POST
def register(request: HttpRequest) -> HttpResponse:
    form = CustomUserCreationForm(data=request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'You can now login')
        return redirect('login')
    else:
        return render(request, 'registration.html', {'form': form})
