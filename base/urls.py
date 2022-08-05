from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('serviceDetail/<int:pk>/', views.serviceDetail, name='serviceDetail'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('faq/', views.fag, name='faq'),
    path('blog/', views.blog, name='blog'),
    path('blogDetail/<int:pk>/', views.blogDetail, name='blogDetail'),
    path('contact/', views.contact, name='contact'),
]