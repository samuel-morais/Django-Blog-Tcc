from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def curso(request):
    return render(request,'curso.html')
