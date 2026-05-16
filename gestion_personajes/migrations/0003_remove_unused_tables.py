from django.db import migrations

SQL_DROP = """
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS accion_combate;
DROP TABLE IF EXISTS turno;
DROP TABLE IF EXISTS tirada_dado;
DROP TABLE IF EXISTS token_mapa;
DROP TABLE IF EXISTS celda;
DROP TABLE IF EXISTS mapa;
DROP TABLE IF EXISTS historia;
DROP TABLE IF EXISTS sesion;
DROP TABLE IF EXISTS mision;
DROP TABLE IF EXISTS combate;
DROP TABLE IF EXISTS campania_jugador;
DROP TABLE IF EXISTS campania;
DROP TABLE IF EXISTS npc;
DROP TABLE IF EXISTS usuario_rol;

SET FOREIGN_KEY_CHECKS = 1;
"""


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_personajes', '0002_add_collaborative_tables'),
    ]

    operations = [
        migrations.RunSQL(
            sql=SQL_DROP,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
