from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('mission/', views.mission, name='mission'),
  path('meetup/', views.meetup, name='meetup'),
  path('meetup/<int:dog_id>/', views.meetup_detail, name='meetup_detail'),
  # path('create/', views.meetupCreate.as_view(), name='meetupcreate'),
  # path('update/', views.meetupUpdate.as_view(), name='meetupUpdate'),
  # path('delete/', views.meetupDelete.as_view(), name='meetupDelete'),
]