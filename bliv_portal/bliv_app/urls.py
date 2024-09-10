"""
URL configuration for bliv_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('home', home),
    path('leitores', aba_leitor),
    path('livros', aba_livros),
    path('save', salvar_estudante),
    path('leitores/add', save_leitor),
    path('adicionar-ao-carrinho/<str:book_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('minha_estante', minha_estante, name='minha_estante'),
]

