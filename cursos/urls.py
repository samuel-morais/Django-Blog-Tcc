
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('<int:curso_id>', views.curso, name='curso'),  #Mapeando a rota de Curso #
    path ('busca', views.buscar,name = 'buscar'),
    path('cria/curso', views.cria_curso, name='cria_curso'),
    path('deleta/<int:curso_id>',views.deleta_curso, name='deleta_curso'),
    path('edita/<int:curso_id>',views.edita_curso, name='edita_curso'),
    path('atualiza_curso', views.atualiza_curso, name='atualiza_curso'),

]