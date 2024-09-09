from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *

def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def shopping(request):
    return HttpResponse("Bem-vindo(a) à Bliv!")

def salvar_estudante(request):
    nome_estudante = request.POST['nome_estudante']
    return render(request, "welcome.html", context={'nome_estudante': nome_estudante})

def aba_leitor(request):
    if request.method=="GET":
        leitores = leitor.objects.all()
        return render(request, "leitores.html", 
                    context={"current_tab": "leitores", "leitores":leitores}
                    )
    
    else:
        query = request.POST['query']
        leitores = leitor.objects.raw("select * from bliv_app_leitor where nome_leitor like '%" + query + "%'")
        return render(request, "leitores.html", 
                    context={"current_tab": "leitores", "leitores":leitores}
                    )

def save_leitor(request):
    leitor_item = leitor(reference_Id=request.POST['ref_Id'],
                         nome_leitor=request.POST['nome'],
                         email_leitor=request.POST['email'],
                         endereco_leitor=request.POST['endereco'],
                         active=True)
    
    leitor_item.save()
    return redirect('/leitores')