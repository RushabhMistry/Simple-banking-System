from django.db import models
from django.db.models.fields import DateField

# Create your models here.
  
class Customer(models.Model):
    user_id         = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=30)
    email           = models.EmailField(max_length=60, unique=True)

class Txnn(models.Model):
    user_id         = models.IntegerField(default="")
    amount          = models.FloatField()
    type            = models.SmallIntegerField(default="")
    narration       = models.CharField(max_length=255)
    date            = models.DateField(auto_now_add=True)
    time            = models.TimeField(auto_now_add=True)

