
from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria/curso', views.cria_curso, name='cria_curso'),
    path('deleta/<int:curso_id>',views.deleta_curso, name='deleta_curso'),

]