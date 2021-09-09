from django.shortcuts import redirect, render
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def mission(request):
  return render(request, 'mission.html')

@login_required
def meetup(request):
  dogs = Dog.objects.all
  return render (request, 'meetup.html', {'dogs': dogs})

@login_required
def meetup_detail(request, dog_id):
  dog=Dog.objects.get(id=dog_id)
  return render(request,'meetup_detail.html', {'dog':dog})


class MeetUpCreate(LoginRequiredMixin,CreateView):
  model = Dog
  fields = '__all__'
  success_url = '/meetup/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class meetupUpdate(LoginRequiredMixin,UpdateView):
  model = Dog
  fields = '__all__'
  success_url = '/meetup'

  
class meetupDelete(LoginRequiredMixin,DeleteView):
  model = Dog
  success_url = '/meetup/'

class Login(LoginView):
  template_name = 'login.html'
  redirect_field_name='home'
  redirect_authenticated_user=True

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('meetup')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)