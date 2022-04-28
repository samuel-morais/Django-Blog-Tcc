
from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria/curso', views.cria_curso, name='cria_curso'),
    path('deleta/<int:curso_id>',views.deleta_curso, name='deleta_curso'),
    path('edita/<int:curso_id>',views.edita_curso, name='edita_curso'),
    path('atualiza_curso', views.atualiza_curso, name='atualiza_curso'),


]