from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect



def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def leitores(request):
    return render(request, "leitores.html", context={"current_tab": "leitores"})

def shopping(request):
    return HttpResponse("Bem-vindo(a) à Bliv!")

def salvar_estudante(request):
    nome_estudante = request.POST['nome_estudante']
    return render(request, "welcome.html", context={'nome_estudante': nome_estudante})
