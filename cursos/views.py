from django.shortcuts import render, get_list_or_404, get_object_or_404
from.models import Curso

# Create your views here.

def index(request):
    cursos = Curso.objects.filter(publicada=True)

    

    dados = {
        'cursos' : cursos
    }
    return render(request, 'index.html',dados)



def curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    curso_a_exibir = {
        'curso' : curso
    }
    return render(request,'curso.html',curso_a_exibir)

