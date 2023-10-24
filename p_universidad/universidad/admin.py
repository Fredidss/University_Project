from django.contrib import admin
from .models import Curso, Carrera, Profesor, Estudiante

admin.site.register(Curso)
admin.site.register(Carrera)
admin.site.register(Profesor)
admin.site.register(Estudiante)

from django.contrib import admin
from django.apps import apps

models = apps.get_models()

class GenericModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models._meta.fields]
    list_filter = [field.name for field in models._meta.fields]
    search_fields = [field.name for field in models._meta.fields]

for model in models:
    admin.site.register(model, GenericModelAdmin)
