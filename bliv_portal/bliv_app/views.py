from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *

def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def aba_livros(request):
    return render(request, "livros.html", context={"current_tab": "livros"})

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

# API DA GOOGLE
from django.http import JsonResponse
from .request import GoogleBooksAPI, formatar_info_livro

def api_livros(request):
    query = request.GET.get('q', 'programming')  # Query padrão para buscar livros relacionados a 'programming'
    google_books = GoogleBooksAPI()
    resultados = google_books.buscar_livros(query)

    livros_formatados = []
    if "items" in resultados:
        livros_formatados = [formatar_info_livro(livro) for livro in resultados["items"]]

    return JsonResponse(livros_formatados, safe=False)

# Adicionar livro ao carrinho
@csrf_exempt
def adicionar_ao_carrinho(request, book_id):
    if request.method == 'POST':
        user = request.user
        # Suponha que o JSON enviado pela API de livros já esteja formatado
        book_data = GoogleBooksAPI().buscar_livros(f"id:{book_id}")
        livro_formatado = formatar_info_livro(book_data["items"][0])  # Pega o primeiro item

        # Adiciona o livro ao carrinho do usuário
        carrinho, created = Carrinho.objects.get_or_create(user=user)
        carrinho.book_data.append(livro_formatado)
        carrinho.save()

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# Exibir a estante (carrinho)
@login_required
def minha_estante(request):
    carrinhos = Carrinho.objects.filter(user=request.user)
    livros = [c.book_data for c in carrinhos]
    
    return render(request, 'minha_estante.html', context={'livros': livros, 'current_tab': 'minha_estante'})