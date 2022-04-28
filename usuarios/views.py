from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from cursos.models import Curso

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            messages.error(request,'O campo Nome não pode ficar em Branco') 
            return redirect('cadastro')
        if not email.strip():
            messages.error(request,'O campo email não pode ficar em Branco') 
            return redirect('cadastro')  
        if senha != senha2:
            messages.error(request,'As senhas não são iguais')    
            return redirect('cadastro') 
        if User.objects.filter(email=email).exists():
            messages.error(request,'Usuário Já Cadastrado') 
            return redirect('cadastro')   
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request,'Usuário Cadastrado com Sucesso !')  
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            messages.error(request,'Os campos email e senha não podem ficar em branco') 
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request,user)     
                messages.success(request,'Login Realizado com Sucesso!!')  
                return redirect('dashboard')
                
     
        
    return render(request,'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect ('index')
    
#    return render(request,'usuarios/logout.html')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        cursos = Curso.objects.order_by('-data_curso').filter(pessoa=id)
       

        dados = { 

            'cursos' : cursos
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')
        

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
       return render (request,'usuarios/cria_curso.html')

        

