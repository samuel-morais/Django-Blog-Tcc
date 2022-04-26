from django.shortcuts import render
from.models import Curso

# Create your views here.

def index(request):
    cursos = Curso.objects.all()

    

    dados = {
        'cursos' : cursos
    }
    return render(request, 'index.html',dados)



def curso(request):
    return render(request,'curso.html')

