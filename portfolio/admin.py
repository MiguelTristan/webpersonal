from django.contrib import admin

# importar 'modelos'
from .models import Project

# Register your models here.

# clase para mostrar campos de solo lectura son configuraciones extendidas de los campos del modelo
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# registro mis modelos para poder mostrarlos en el panel 'administrador'
admin.site.register(Project, ProjectAdmin)
