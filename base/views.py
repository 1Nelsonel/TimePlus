from django.shortcuts import render
from requests import request

# Create your views here.


def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def service(request):
    context = {}
    return render(request, 'base/service.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def team(request):
    context = {}
    return render(request, 'base/team.html', context)
