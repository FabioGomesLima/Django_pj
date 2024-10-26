from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Pessoa
from django.db.models import Q #import para o operador or

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        pessoa = Pessoa(
            nome=nome,
            email=email,
            senha=senha
        )

        pessoa.save()  # Salva a instância no banco de dados
        return HttpResponse('Você foi cadastrado')
    
def listar(request):
    pessoas = Pessoa.objects.filter( nome = 'fabio').filter(Q(senha = 'fb12345') | Q (senha = '12345')).exclude(senha = 'fb12345')
    print(pessoas)
    return render(request, 'listar/listar.html', { 'pessoas':pessoas})