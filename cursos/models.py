from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create Modelo de Cursos


class Curso(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_curso = models.CharField(max_length=200)
    ementa_do_curso = models.TextField()
    informacoes = models.TextField()
    carga_horaria = models.IntegerField()
    categoria= models.CharField(max_length=100)
    data_curso = models.DateTimeField(default=datetime.now, blank=True)
    foto_curso = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank = True)
    publicada= models.BooleanField(default=False)
    def __str__(self):
        return self.nome_curso