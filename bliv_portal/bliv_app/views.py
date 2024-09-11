from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import *
from perfil import *

# IR PRAS PÁGINAS
def home(request):
    return render(request, "home.html", context={"current_tab": "home"})

def aba_livros(request):
    return render(request, "livros.html", context={"current_tab": "livros"})

def criar(request):
    return render(request, 'criar.html')

def minha_estante(request):
    # Se você quiser exibir os livros do carrinho do usuário logado
    if request.user.is_authenticated:
        carrinho = Carrinho.objects.filter(user=request.user)
    else:
        carrinho = None

    return render(request, 'minha_estante.html', {'carrinho': carrinho})

# PÁGINA LEITORES
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

# DETALHES DO LIVRO
def detalhe_livro(request, book_id):
    # Instancia a API do Google Books
    api = GoogleBooksAPI()
    
    # Busca o livro pelo ID
    resposta = api.buscar_livros(book_id)
    
    # Verifica se o livro foi encontrado
    if not resposta.get("items"):
        return render(request, "404.html", status=404)  # Página de erro 404
    
    # Como a API retorna uma lista de resultados, pegamos o primeiro livro
    livro = resposta["items"][0]
    
    # Formata as informações do livro
    livro_formatado = formatar_info_livro(livro)
    
    return render(request, 'detalhe_livro.html', {'livro': livro_formatado})

# ADICIONAR LIVROS AO CARRINHO

@login_required  # O usuário precisa estar logado
@require_POST  # Apenas aceita requisições POST
def adicionar_ao_carrinho(request, book_id):
    # Instancia a API do Google Books
    api = GoogleBooksAPI()
    
    # Busca o livro pelo ID
    resposta = api.buscar_livros(book_id)

    # Verifica se o livro foi encontrado
    if not resposta.get("items"):
        return JsonResponse({"error": "Livro não encontrado."}, status=404)

    # Como a API retorna uma lista de resultados, pegamos o primeiro livro
    livro = resposta["items"][0]

    # Formata as informações do livro para adicionar ao carrinho
    livro_formatado = formatar_info_livro(livro)

    # Obtém ou cria um carrinho para o usuário autenticado
    carrinho, created = Carrinho.objects.get_or_create(user=request.user)

    # Verifica se o livro já está no carrinho (evita duplicatas)
    if livro_formatado['id'] not in [item['id'] for item in carrinho.book_data]:
        # Adiciona o livro ao carrinho
        carrinho.book_data.append(livro_formatado)
        carrinho.save()

    # Retorna uma resposta JSON de sucesso
    return JsonResponse({'message': 'Livro adicionado ao carrinho com sucesso!'})
