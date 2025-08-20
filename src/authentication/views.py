from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST

from src.authentication.forms.custom_user_creation_form import CustomUserCreationForm

REMEMBER_ME = 2592000


@require_GET
def loginForm(request: HttpRequest) -> HttpResponse:
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@require_POST
def login(request: HttpRequest) -> HttpResponse:
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        # remember me
        request.session.set_expiry(REMEMBER_ME)
        return redirect('dashboard')
    else:
        return render(request, 'login.html', {'form': form})


@require_GET
def registrationForm(request: HttpRequest) -> HttpResponse:
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


@require_GET
def forgotPasswordForm(request: HttpRequest) -> HttpResponse:
    form = PasswordResetForm()
    return render(request, 'forgot_password.html', {'form': form})


@require_POST
def forgotPassword(request: HttpRequest) -> HttpResponse:
    form = PasswordResetForm(data=request.POST)
    if form.is_valid():
        form.save(
            request=request,
            use_https=request.is_secure()
        )
        messages.success(request, 'We\'ve emailed you instructions for resetting your password.')
        return redirect('login')
    else:
        return render(request, 'forgot_password.html', {'form': form})
