from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.ver_cursos, name='ver_cursos'),
    path('carreras/', views.ver_carreras, name='ver_carreras'),
    path('profesores/', views.ver_profesores, name='ver_profesores'),
    path('estudiantes/', views.ver_estudiantes, name='ver_estudiantes'),
]
