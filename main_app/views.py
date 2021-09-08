from django.shortcuts import render
# Add the following import
from .models import Dog

# Define the home view
def home(request):
  return render(request, 'home.html')

def mission(request):
  return render(request, 'mission.html')

def training(request):
  return render (request, 'training.html')

def meetup(request):
  dogs=Dog.objects.all
  return render (request, 'meetup.html', {'dogs':dogs})
