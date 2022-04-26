from django.contrib import admin

from .models import Curso

# Alterando a lista de Curso Admin
class ListandoCursos(admin.ModelAdmin):
    list_display = ('id','nome_curso','categoria','carga_horaria')
    list_display_links = ('id','nome_curso')

admin.site.register(Curso,ListandoCursos)