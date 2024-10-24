from django.shortcuts import render
from django.http import HttpResponse
import json


def cadastro(request):
    erro = request.GET.get('erro')
    print(erro)
    return render(request, 'cadastro/index.html', {'erro':erro})


def valida_formulario(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    return HttpResponse(json.dumps({'nome':nome, 'email':email}))