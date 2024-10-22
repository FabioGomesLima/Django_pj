from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    nome = 'Fabio'
    idade = '22'
    profissao = 'Programador'
    dicionario = {'nome': nome, #dicionário
                  'idade': idade, 
                  'profissao':profissao}
    
    return render(request, 'cadastro/index.html', { 'nome': nome, #dicionário
                                                   'idade':idade,
                                                   'profissao':profissao
                                                             })