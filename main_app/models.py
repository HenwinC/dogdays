from django.db import models

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

# Create your models here.
