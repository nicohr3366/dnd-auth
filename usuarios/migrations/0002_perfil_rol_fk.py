import django.db.models.deletion
from django.db import migrations, models


def crear_roles_base_y_migrar(apps, schema_editor):
    Rol = apps.get_model('usuarios', 'Rol')
    PerfilUsuario = apps.get_model('usuarios', 'PerfilUsuario')

    jugador, _ = Rol.objects.get_or_create(nombre='Jugador', defaults={'descripcion': ''})
    narrador, _ = Rol.objects.get_or_create(nombre='Narrador', defaults={'descripcion': ''})
    administrador, _ = Rol.objects.get_or_create(nombre='Administrador', defaults={'descripcion': ''})

    mapa = {
        'jugador': jugador,
        'narrador': narrador,
        'administrador': administrador,
    }

    for perfil in PerfilUsuario.objects.all():
        clave = perfil.rol_old.lower() if perfil.rol_old else 'jugador'
        perfil.rol_new = mapa.get(clave, jugador)
        perfil.save()


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        # Paso 1: renombrar el campo antiguo
        migrations.RenameField(
            model_name='perfilusuario',
            old_name='rol',
            new_name='rol_old',
        ),
        # Paso 2: agregar el nuevo campo FK nullable
        migrations.AddField(
            model_name='perfilusuario',
            name='rol_new',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='perfiles',
                to='usuarios.rol',
            ),
        ),
        # Paso 3: migrar datos y crear roles base
        migrations.RunPython(crear_roles_base_y_migrar, migrations.RunPython.noop),
        # Paso 4: eliminar campo antiguo
        migrations.RemoveField(
            model_name='perfilusuario',
            name='rol_old',
        ),
        # Paso 5: renombrar el nuevo campo a 'rol'
        migrations.RenameField(
            model_name='perfilusuario',
            old_name='rol_new',
            new_name='rol',
        ),
    ]
