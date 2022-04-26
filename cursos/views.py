from django.shortcuts import render, get_list_or_404, get_object_or_404
from.models import Curso

# Create your views here.

def index(request):
    cursos = Curso.objects.order_by('-data_curso').filter(publicada=True)

    

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

def buscar(request):
    lista_cursos = Curso.objects.order_by('-data_curso').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_cursos = lista_cursos.filter(nome_curso__icontains = nome_a_buscar)

        dados = {
               'cursos' : lista_cursos
        }

    return render(request,'buscar.html', dados)

