from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  age = models.IntegerField()
  temperment = models.CharField(max_length=100)
  training = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  sex = models.CharField(max_length=1)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  
def __str__(self):
  return self.name

def get_absolute_url(self):
    return reverse('meetup_detail', kwargs={'dog_id': self.id})

