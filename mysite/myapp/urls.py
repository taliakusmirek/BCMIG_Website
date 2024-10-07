from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eboard/', views.eboard, name='eboard'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('contact-view/', views.contact_view, name='contact_view'),
    path('resources/', views.resources, name='resources'),
    path('lectures/', views.lectures, name='lectures'),
    path('workshops/', views.workshops, name='workshops'),
]