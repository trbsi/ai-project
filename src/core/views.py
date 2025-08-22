from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('user_settings')
    else:
        return redirect('login')

def about(request):
    return render(request, 'about.html')