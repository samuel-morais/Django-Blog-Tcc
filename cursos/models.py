from django.db import models
from datetime import datetime
from pessoas.models import Pessoa
# Create Modelo de Cursos


class Curso(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_curso = models.CharField(max_length=200)
    ementa_do_curso = models.TextField()
    informacoes = models.TextField()
    carga_horaria = models.IntegerField()
    categoria= models.CharField(max_length=100)
    data_curso = models.DateTimeField(default=datetime.now, blank=True)