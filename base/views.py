from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages

from base.models import Message, Blog, Comment, Service


# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
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
    blogs = Blog.objects.all()
    comments = Comment.objects.all()
    paginator = Paginator(blogs, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'blogs': blogs, 'page_obj': page_obj, 'comments': comments}
    return render(request, 'base/blog.html', context)


def blogDetail(request, pk):
    blog = Blog.objects.get(id=pk)
    services = Service.objects.all()
    comments = blog.comment_set.all()
    blogs = Blog.objects.all()
    services = Service.objects.all()

    if request.method == 'POST':
        comment = Comment.objects.create(
            blog=blog,
            user=request.POST.get('user'),
            email=request.POST.get('email'),
            body=request.POST.get('body'),
        )

        messages.success(request, 'Message sent')
        return redirect('blogDetail', pk=blog.id)

    context = {'blog': blog, 'services': services,
               'comments': comments, 'blogs': blogs, }

    return render(request, 'base/blog-detail.html', context)


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
