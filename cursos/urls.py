
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('<int:curso_id>', views.curso, name='curso'),  #Mapeando a rota de Curso #
]