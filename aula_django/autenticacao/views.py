from django.shortcuts import render
from django.http import HttpResponse
from aula_django.settings import BASE_DIR
import os

def cadastro(request):
    print(os.path.join(BASE_DIR,'templates'))
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
    
    
    return render(request, 'cadastro/index.html',{ 'pessoas':pessoa,
                                                       'x': 0 
                                                              })