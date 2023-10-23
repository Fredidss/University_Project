from django.contrib import admin
from .models import Curso, Carrera, Profesor, Estudiante

admin.site.register(Curso)
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Estudiante)
# Register your models here.
from django.contrib import admin
from django.apps import apps

# Obtiene todos los modelos registrados en la aplicación
models = apps.get_models()

# Define una clase de administrador genérica
class GenericModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models._meta.fields]
    list_filter = [field.name for field in models._meta.fields]
    search_fields = [field.name for field in models._meta.fields]

# Registra todos los modelos con la clase de administrador genérica
for model in models:
    admin.site.register(model, GenericModelAdmin)
