from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    pessoa =[ 
                {'nome':'Fabio ',
                'idade':'22',
                'profissao':'Programador'
                               },
             {'nome':'Fabio Gomes ',
                'idade':'22',
                'profissao':'Front End'
                               } 
            ]
    
    
    return render(request, 'cadastro/index.html', { 'pessoa':pessoa
                                                             })