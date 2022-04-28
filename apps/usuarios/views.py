from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from cursos.models import Curso


def cadastro(request):
    """Cadastra uma Nova Pessoa no Sistema"""
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request,'O campo Nome não pode ficar em Branco') 
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request,'O campo email não pode ficar em Branco') 
            return redirect('cadastro')  
        if senha_nao_sao_iguais(senha, senha2):
            messages.error(request,'As senhas não são iguais')    
            return redirect('cadastro') 
        if User.objects.filter(email=email).exists():
            messages.error(request,'Usuário Já Cadastrado') 
            return redirect('cadastro')  
        if User.objects.filter(username=nome).exists():
            messages.error(request,'Usuário Já Cadastrado') 
            return redirect('cadastro')      
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request,'Usuário Cadastrado com Sucesso !')  
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    """Realiza o Login no Sistema"""
    
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
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
    """Realiza o Logoutno Sistema"""
    auth.logout(request)
    messages.success(request,'Logout realizado com sucesso !')
    return redirect ('index')
    
#    return render(request,'usuarios/logout.html')

def dashboard(request):
    """Dashboard de cursos Sistema"""
    if request.user.is_authenticated:
        id = request.user.id
        cursos = Curso.objects.order_by('-data_curso').filter(pessoa=id)
       

        dados = { 

            'cursos' : cursos
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')
        



def campo_vazio(campo):
    return  not campo.strip()

def senha_nao_sao_iguais(senha, senha2):
    return senha != senha2
        





