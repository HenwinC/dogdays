from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Puppy lovers</h1>')

def mission(request):
  return render(request, 'mission.html')

def training(request):
  return render (request, 'training.html')

