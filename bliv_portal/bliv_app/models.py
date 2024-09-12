from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
# Create your models here.

class leitor(models.Model):

    def __str__(self):
        return self.nome_leitor + " " + "|" + " " + self.email_leitor

    reference_Id=models.CharField(max_length=200)
    nome_leitor=models.CharField(max_length=200)
    email_leitor=models.TextField(max_length=200)
    endereco_leitor=models.TextField()
    senha = models.CharField(max_length=16, default='12345678')
    active=models.BooleanField(default=True)

    def check_password(self, password):
        return check_password(password, self.senha)

    def set_password(self, raw_password):
        self.senha = make_password(raw_password)
        self.save()

# Modelos para os Livros

def upload_image_book(instance, filename):
    return f"{instance.id_book}-{filename}"

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_book, blank=True, null=True)

# Carrinho de Livros

class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_data = models.JSONField(default=list)  # Certifica-se que é uma lista de livros
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho de {self.user.username}"