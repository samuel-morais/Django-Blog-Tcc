
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path ('<int:curso_id>', curso, name='curso'),  #Mapeando a rota de Curso #
    path ('busca', buscar,name = 'buscar'),
    path('cria/curso', cria_curso, name='cria_curso'),
    path('deleta/<int:curso_id>',deleta_curso, name='deleta_curso'),
    path('edita/<int:curso_id>',edita_curso, name='edita_curso'),
    path('atualiza_curso', atualiza_curso, name='atualiza_curso'),

]