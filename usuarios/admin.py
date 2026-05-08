from django.contrib import admin
from .models import Rol, PerfilUsuario


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_creacion')
    search_fields = ('nombre',)


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol')
    list_filter = ('rol',)
    search_fields = ('usuario__username',)
