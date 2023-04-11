from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import quote
from base.models import Appointment, Faq, Message, Blog, Comment, Service


# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'base/home.html', context)


def service(request):

    services = Service.objects.all()

    if request.method == 'POST':
        appoitment = Appointment.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            body=request.POST.get('body'),
            ptype=request.POST.get('ptype'),
            bedroom=request.POST.get('bedroom'),
            frequency=request.POST.get('frequency'),
            time=request.POST.get('time'),
            date=request.POST.get('date'),
        )

        messages.success(
            request, 'Your book an appointment successfully. Thank you!')
        return redirect('service')
    context = {'services': services }
    return render(request, 'base/service.html', context)

def serviceDetail(request, pk):
    service = Service.objects.get(id=pk)
    services = Service.objects.all()

    if request.method == 'POST':
        phone_number = '254798616085'  # Replace with your phone number
        service_name = request.POST.get('service_name')
        service = Service.objects.get(name=service_name)

        service_link = request.build_absolute_uri(service.get_absolute_url())
        whatsapp_message = f'I am interested in the:\n*{service.name.capitalize()}* service.\nPlease contact me.\n\nService link:\n{service_link}'

        whatsapp_url = f'https://wa.me/{phone_number}?text={quote(whatsapp_message)}'
        return HttpResponseRedirect(whatsapp_url)
    
    context = {'service': service, 'services': services}
    return render(request, 'base/service-detail.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)


def team(request):
    context = {}
    return render(request, 'base/team.html', context)


def fag(request):
    faqs = Faq.objects.all()
    context = {'faqs': faqs}
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



