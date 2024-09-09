from django.db import models

# Create your models here.

class leitor(models.Model):

    def __str__(self):
        return self.nome_leitor + " " + "|" + " " + self.email_leitor

    reference_Id=models.CharField(max_length=200)
    nome_leitor=models.CharField(max_length=200)
    email_leitor=models.TextField(max_length=200)
    endereco_leitor=models.TextField()
    active=models.BooleanField(default=True)
