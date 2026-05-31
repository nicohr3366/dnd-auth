import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_perfil_rol_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
