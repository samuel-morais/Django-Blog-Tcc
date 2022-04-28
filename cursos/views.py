from django.shortcuts import render,redirect, get_list_or_404, get_object_or_404
from.models import Curso
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.

def index(request):
    cursos = Curso.objects.order_by('-data_curso').filter(publicada=True)

    

    dados = {
        'cursos' : cursos
    }
    return render(request, 'cursos/index.html',dados)



def curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    curso_a_exibir = {
        'curso' : curso
    }
    return render(request,'cursos/curso.html',curso_a_exibir)

def buscar(request):
    lista_cursos = Curso.objects.order_by('-data_curso').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_cursos = lista_cursos.filter(nome_curso__icontains = nome_a_buscar)

        dados = {
               'cursos' : lista_cursos
        }

    return render(request,'cursos/buscar.html', dados)

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