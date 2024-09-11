from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
   usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
   data_nascimento = models.DateField()
  
   def __str__(self):
       return f'{self.usuario}'
   
   class Meta():
       verbose_name = 'Perfil'
       verbose_name_plural = 'Perfis'