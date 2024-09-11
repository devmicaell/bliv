from django.shortcuts import render

def cadastro(request):
    if request.method == "GET":
        return render (request, 'perfil/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')


def login(request):
    return render(request, 'perfil/login.html')


    #ve se abre o site
    #ve se foi, só qro q abra o cadastro pelo menos