from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages

from base.models import Message

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


def fag(request):
    context = {}
    return render(request, 'base/faq.html', context)


def blog(request):
    context = {}
    return render(request, 'base/blog.html', context)


def contact(request):
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.POST.get('user'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            body=request.POST.get('body'),
        )
        
        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('contact')
    context = {}
    return render(request, 'base/contact.html', context)