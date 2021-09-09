from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from django.urls import reverse

# Define the home view
def home(request):
  return render(request, 'home.html')

def mission(request):
  return render(request, 'mission.html')

def meetup(request):
  dogs = Dog.objects.all
  return render (request, 'meetup.html', {'dogs': dogs})

def meetup_detail(request, dog_id):
  dog=Dog.objects.get(id=dog_id)
  return render(request,'meetup_detail.html', {'dog':dog})

  
# class meetupCreate(CreateView):
#   model = Dog
#   fields = '__all__'
#   template_name = 'dog_form.html'
#   success_url = '/meetup/dog_form'

# class meetupDelete(DeleteView):
#   model = Dog
#   success_url = '/meetup/'
  
# class meetupUpdate(UpdateView):
#   model = Dog
#   fields = '__all__'
#   success_url = '/meetup'
  