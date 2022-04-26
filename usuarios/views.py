from django.shortcuts import render,redirect
from django.contrib.auth.models import User

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
    return render(request,'usuarios/login.html')

def logout(request):
    pass
#    return render(request,'usuarios/logout.html')

def dashboard(request):
    pass
#    return render(request,'usuarios/dashboard.html')  


