from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('meetup/', views.meetup, name='meetup'),
  path('login/', views.Login.as_view(), name='loginuser'),
  path('signup/', views.signup, name='signup'),
  path('meetup/<int:dog_id>/', views.meetup_detail, name='meetup_detail'),
  path('meetup/create/', views.MeetUpCreate.as_view(), name='meetup_create'),
  path('meetup/<int:pk>/update/', views.meetupUpdate.as_view(), name='meetup_update'),
  path('meetup/<int:pk>/delete/', views.meetupDelete.as_view(), name='meetup_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]