from django.contrib import admin

from .models import Curso

# Alterando a lista de Curso Admin
class ListandoCursos(admin.ModelAdmin):
    list_display = ('id','nome_curso','categoria','carga_horaria')
    list_display_links = ('id','nome_curso')
    search_fields = ('nome_curso',) 
    list_filter = ('categoria',)
    list_per_page = 10

admin.site.register(Curso,ListandoCursos)