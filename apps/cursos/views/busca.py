from cursos.models import Curso
from django.shortcuts import render,redirect, get_list_or_404, get_object_or_404


def buscar(request):
    lista_cursos = Curso.objects.order_by('-data_curso').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_cursos = lista_cursos.filter(nome_curso__icontains = nome_a_buscar)

        dados = {
               'cursos' : lista_cursos
        }

    return render(request,'cursos/buscar.html', dados)