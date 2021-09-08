from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('mission/', views.mission, name='mission'),
  path('training/', views.training, name='training'),
  path ('meetup/', views.meetup, name='meetup'),
]