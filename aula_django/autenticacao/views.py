from django.shortcuts import render
from django.http import HttpResponse


def cadastro(request):
    erro = request.GET.get('erro')
    
    
    
    return render(request, 'cadastro/index.html', {'erro':erro})