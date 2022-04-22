from django.db import models
from datetime import datetime
# Create Modelo de Cursos

class Cursos(models.Model):
    nome_curso = models.CharField(max_length=200)
    ementa_do_curso = models.TextField()
    informacoes = models.TextField()
    carga_horaria = models.IntegerField()
    categoria= models.CharField(max_length=100)
    data_curso = models.DateTimeField(default=datetime.now, blank=True)