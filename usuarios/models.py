from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Rol(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class SolicitudEdicionRol(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='solicitudes')
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes_rol')
    nombre_nuevo = models.CharField(max_length=100)
    descripcion_nueva = models.TextField(blank=True)
    motivo = models.TextField(blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fecha_solicitud = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-fecha_solicitud']
        verbose_name = 'Solicitud de Edición de Rol'
        verbose_name_plural = 'Solicitudes de Edición de Roles'

    def __str__(self):
        return f"{self.solicitante.username} → {self.rol.nombre} ({self.estado})"


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name='perfiles')

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'

    def __str__(self):
        rol_nombre = self.rol.nombre if self.rol else 'Sin rol'
        return f"{self.usuario.username} ({rol_nombre})"
