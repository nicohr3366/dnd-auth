from django.db import models
from django.contrib.auth.models import User


class Rol(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name='perfiles')

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuario'

    def __str__(self):
        rol_nombre = self.rol.nombre if self.rol else 'Sin rol'
        return f"{self.usuario.username} ({rol_nombre})"


# ========== GESTION DE PERSONAJES ==========

# =========================
# RAZA
# =========================
class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(blank=True)

    bono_fuerza = models.IntegerField(default=0)
    bono_destreza = models.IntegerField(default=0)
    bono_constitucion = models.IntegerField(default=0)
    bono_inteligencia = models.IntegerField(default=0)
    bono_sabiduria = models.IntegerField(default=0)
    bono_carisma = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'raza'


# =========================
# CLASE
# =========================
class Clase(models.Model):
    id_clase = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(blank=True)
    dado_vida = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'clase'


# =========================
# HABILIDAD
# =========================
class Habilidad(models.Model):
    id_habilidad = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'habilidad'


# =========================
# PERSONAJE
# =========================
class Personaje(models.Model):
    id_personaje = models.AutoField(primary_key=True)

    nombre = models.CharField(max_length=100)

    nivel = models.IntegerField(default=1)
    experiencia = models.IntegerField(default=0)

    vida_actual = models.IntegerField(default=10)
    vida_maxima = models.IntegerField(default=10)

    fuerza = models.IntegerField(default=10)
    destreza = models.IntegerField(default=10)
    constitucion = models.IntegerField(default=10)
    inteligencia = models.IntegerField(default=10)
    sabiduria = models.IntegerField(default=10)
    carisma = models.IntegerField(default=10)

    # Relaciones
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    raza = models.ForeignKey(Raza, on_delete=models.PROTECT, db_column='id_raza')
    clase = models.ForeignKey(Clase, on_delete=models.PROTECT, db_column='id_clase')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'personaje'


# =========================
# RELACIÓN MANY TO MANY
# =========================
class PersonajeHabilidad(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE)

    class Meta:
        db_table = 'personaje_habilidad'
        unique_together = ('personaje', 'habilidad')