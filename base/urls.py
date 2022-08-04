from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('faq/', views.fag, name='faq'),
]