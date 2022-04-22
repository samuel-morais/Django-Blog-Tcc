from django.shortcuts import render

# Create your views here.

def index(request):
    cursos = {
        1:'Python',
        2:'PHP',
        3:'Html'
    }  

    dados = {
        'nome_dos_cursos' : cursos
    }
    return render(request, 'index.html',dados)



def curso(request):
    return render(request,'curso.html')

