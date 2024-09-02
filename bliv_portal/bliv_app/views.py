from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect



def home(request):
    return HttpResponse("Hello World")

def shopping(request):
    return HttpResponse("Bem-vindo(a) à Bliv!")
