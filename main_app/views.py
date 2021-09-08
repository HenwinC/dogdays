from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Puppy lovers</h1>')

def mission(request):
  return HttpResponse('<h2>Our mission is to bring dog lovers together and make socializing dogs safe and fun for all</h2>')

