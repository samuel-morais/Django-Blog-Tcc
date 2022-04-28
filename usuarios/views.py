from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em Branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em Branco')
            return redirect('cadastro')  
        if senha != senha2:
            print('As senhas não são iguais')     
            return redirect('cadastro') 
        if User.objects.filter(email=email).exists():
            print ("Usuário Já Cadastrado")
            return redirect('cadastro')   
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print("Usuário Cadastrado com Sucesso !")    
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email,senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request,user)     
                print("Login Realizado com Sucesso!!")   
                return redirect('dashboard')
     
        
    return render(request,'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect ('index')
    
#    return render(request,'usuarios/logout.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render (request,'usuarios/dashboard.html')
    else:
        return redirect('index')
#    return render(request,'usuarios/dashboard.html')  

def cria_curso(request):
    if request.method == 'POST':
        nome_curso = request.POST['nome_curso']
        ementa_curso = request.POST['ementa_curso']
        informacoes = request.POST['informacoes']
        carga_horaria = request.POST['carga_horaria']
        categoria = request.POST['categoria']
        foto_curso = request.FILES['foto_curso']
        print(nome_curso,ementa_curso,informacoes,carga_horaria,categoria,foto_curso)
        return redirect('dashboard')
    else:
       return render (request,'usuarios/cria_curso.html')

        

