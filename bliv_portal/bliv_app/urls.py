from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home),
    path('home', home),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('leitores', aba_leitor),
    path('livros', aba_livros),
    path('leitores/add', save_leitor),
    path('minha_estante', minha_estante),  # Defina sua view 'minha_estante'
    path('detalhe_livro/<str:book_id>/', detalhe_livro),
    path('adicionar-ao-carrinho/<str:book_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
]