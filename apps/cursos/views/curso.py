from django.shortcuts import render,redirect, get_list_or_404, get_object_or_404
from cursos.models import Curso
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger

# Create your views here.

def index(request):
    cursos = Curso.objects.order_by('-data_curso').filter(publicada=True)
    paginator = Paginator(cursos, 1)
    page = request.GET.get('page')
    cursos_por_pagina = paginator.get_page(page)
    

    dados = {
        'cursos' : cursos_por_pagina
    }
    return render(request, 'cursos/index.html',dados)



def curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    curso_a_exibir = {
        'curso' : curso
    }
    return render(request,'cursos/curso.html',curso_a_exibir)



def cria_curso(request):
    if request.method == 'POST':
        nome_curso = request.POST['nome_curso']
        ementa_do_curso = request.POST['ementa_do_curso']
        informacoes = request.POST['informacoes']
        carga_horaria = request.POST['carga_horaria']
        categoria = request.POST['categoria']
        foto_curso = request.FILES['foto_curso']
        #pegando as informações do usuário
        user = get_object_or_404(User, pk=request.user.id)
        #criando objeto de receita
        curso = Curso.objects.create(pessoa=user,nome_curso = nome_curso, ementa_do_curso = ementa_do_curso, informacoes = informacoes, carga_horaria = carga_horaria,categoria = categoria,foto_curso = foto_curso)
        curso.save()
        return redirect('dashboard')
    else:
       return render (request,'cursos/cria_curso.html')

def deleta_curso(request,curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    curso.delete()
    return redirect('dashboard')

def edita_curso(request,curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    curso_a_editar = {'curso':curso}
    return render (request,'cursos/edita_curso.html',curso_a_editar)

def atualiza_curso(request):
    if request.method == 'POST':
        curso_id = request.POST['curso_id']
        r = Curso.objects.get(pk=curso_id)
        r.nome_curso = request.POST['nome_curso']
        r.ementa_do_curso = request.POST['ementa_do_curso']
        r.informacoes = request.POST['informacoes']
        r.carga_horaria = request.POST['carga_horaria']
        r.categoria = request.POST['categoria']
        if 'foto_curso' in request.FILES:
            r.foto_curso = request.FILES['foto_curso']
        r.save()
        return redirect('dashboard')       