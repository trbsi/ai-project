from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')