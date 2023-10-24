from django.db import models
from django.contrib.auth.models import User

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        app_label = 'p_universidad'

class Estudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    edad = models.IntegerField()

class Profesor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    area_especializacion = models.CharField(max_length=100)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
