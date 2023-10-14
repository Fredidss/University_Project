from django.shortcuts import render
from .models import Curso, Estudiante, Profesor, Carrera

def ver_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def ver_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

def ver_carreras(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras.html', {'carreras': carreras})

def ver_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {'profesores': profesores})
