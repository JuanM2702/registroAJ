from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.contrib.auth.models import AbstractUser




class regis(models.Model):
  ml = models.CharField(max_length=50, default='')
  nombre_pc = models.CharField(max_length=50, default='')
  nombre_user = models.CharField(max_length=50, default='')
  cedula = models.IntegerField(default=0)
  centro_costos = models.CharField(max_length=50, default='')
  departamento = models.CharField(max_length=50, default='')
  sede = models.CharField(max_length=50, default='')




  def __str__(self):
    return self.ml




class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created = models.DateTimeField(default=timezone.now)
    datecompleted = models.DateTimeField(null=True, blank=True)
      
      
def __str__(self):
     return self.user





    

