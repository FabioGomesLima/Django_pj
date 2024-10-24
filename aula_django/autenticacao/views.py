from django.shortcuts import render
from django.http import HttpResponse


def cadastro(request):
    nome = request.GET.get('nome')
    sobrenome = request.GET.get('sobrenome')
    idade = request.GET.get('idade')
    
    
    return render(request, 'cadastro/index.html', {'nome':nome,'sobrenome':sobrenome,'idade':idade
                                                                                                  })