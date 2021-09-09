from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('mission/', views.mission, name='mission'),
  path('meetup/', views.meetup, name='meetup'),
  path('meetup/<int:dog_id>/', views.meetup_detail, name='meetup_detail'),
  path('meetup/create/', views.MeetUpCreate.as_view(), name='meetup_create'),
  path('meetup/<int:pk>/update/', views.meetupUpdate.as_view(), name='meetup_update'),
  path('meetup/<int:pk>/delete/', views.meetupDelete.as_view(), name='meetup_delete'),
]