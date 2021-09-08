from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('mission/', views.mission, name='mission'),
  path('training/', views.training, name='training'),
  path ('meetup/', views.meetup, name='meetup'),
  # path('meetup/create/', views.meetupcreate.as_view(), name='meetupcreate'),
  # path('meetup/<int:pk>/update/', views.meetupUpdate.as_view(), name='meetupUpdate'),
  # path('meetup/<int:pk>/delete/', views.meetupDelete.as_view(), name='meetupDelete'),
]