from django.db import models
from django.urls import reverse

class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  age = models.IntegerField()
  temperment = models.TextField(max_length=150)
  training = models.TextField(max_length=150)
  description = models.TextField(max_length=250)
  sex = models.TextField(max_length=1)

def __str__(self):
  return self.name

def get_absolute_url(self):
    return reverse('meetup_detail', kwargs={'dog_id': self.id})

