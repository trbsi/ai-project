from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.


def loginForm(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())