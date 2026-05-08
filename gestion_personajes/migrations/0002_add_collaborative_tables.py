from django.db import migrations


SQL_CREATE_MISSING_TABLES = """
CREATE TABLE IF NOT EXISTS usuario_rol (
    id_usuario_rol INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    id_rol INT NOT NULL,
    CONSTRAINT fk_usuario_rol_user FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE,
    CONSTRAINT fk_usuario_rol_rol FOREIGN KEY (id_rol) REFERENCES rol(id_rol) ON DELETE CASCADE,
    UNIQUE KEY uq_usuario_rol (user_id, id_rol)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS npc (
    id_npc INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50),
    nivel INT DEFAULT 1,
    descripcion TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS campania (
    id_campania INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE,
    estado VARCHAR(50) DEFAULT 'Activa',
    narrador_id INT NOT NULL,
    CONSTRAINT fk_campania_narrador FOREIGN KEY (narrador_id) REFERENCES auth_user(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS campania_jugador (
    id_campania INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id_campania, user_id),
    CONSTRAINT fk_cj_campania FOREIGN KEY (id_campania) REFERENCES campania(id_campania) ON DELETE CASCADE,
    CONSTRAINT fk_cj_user FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS mision (
    id_mision INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(120) NOT NULL,
    descripcion TEXT,
    estado VARCHAR(50) DEFAULT 'Pendiente',
    recompensa VARCHAR(255),
    id_campania INT NOT NULL,
    CONSTRAINT fk_mision_campania FOREIGN KEY (id_campania) REFERENCES campania(id_campania) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS sesion (
    id_sesion INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL,
    resumen TEXT,
    id_campania INT NOT NULL,
    CONSTRAINT fk_sesion_campania FOREIGN KEY (id_campania) REFERENCES campania(id_campania) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS historia (
    id_historia INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(120),
    contenido TEXT,
    id_campania INT NOT NULL,
    CONSTRAINT fk_historia_campania FOREIGN KEY (id_campania) REFERENCES campania(id_campania) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS mapa (
    id_mapa INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    filas INT NOT NULL,
    columnas INT NOT NULL,
    imagen_fondo VARCHAR(255),
    id_campania INT NOT NULL,
    CONSTRAINT fk_mapa_campania FOREIGN KEY (id_campania) REFERENCES campania(id_campania) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS celda (
    id_celda INT AUTO_INCREMENT PRIMARY KEY,
    fila_pos INT NOT NULL,
    columna_pos INT NOT NULL,
    tipo_terreno VARCHAR(50),
    bloqueada BOOLEAN DEFAULT FALSE,
    id_mapa INT NOT NULL,
    CONSTRAINT fk_celda_mapa FOREIGN KEY (id_mapa) REFERENCES mapa(id_mapa) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS token_mapa (
    id_token INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    referencia_id INT,
    pos_x INT NOT NULL,
    pos_y INT NOT NULL,
    id_mapa INT NOT NULL,
    CONSTRAINT fk_token_mapa FOREIGN KEY (id_mapa) REFERENCES mapa(id_mapa) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS combate (
    id_combate INT AUTO_INCREMENT PRIMARY KEY,
    fecha_inicio DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(50) DEFAULT 'Activo',
    id_campania INT NOT NULL,
    CONSTRAINT fk_combate_campania FOREIGN KEY (id_campania) REFERENCES campania(id_campania) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS turno (
    id_turno INT AUTO_INCREMENT PRIMARY KEY,
    orden_turno INT NOT NULL,
    id_combate INT NOT NULL,
    id_personaje BIGINT NULL,
    id_npc INT NULL,
    CONSTRAINT fk_turno_combate FOREIGN KEY (id_combate) REFERENCES combate(id_combate) ON DELETE CASCADE,
    CONSTRAINT fk_turno_personaje FOREIGN KEY (id_personaje) REFERENCES personaje(id) ON DELETE CASCADE,
    CONSTRAINT fk_turno_npc FOREIGN KEY (id_npc) REFERENCES npc(id_npc) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS tirada_dado (
    id_tirada INT AUTO_INCREMENT PRIMARY KEY,
    tipo_dado VARCHAR(10) NOT NULL,
    resultado INT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    CONSTRAINT fk_tirada_user FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS accion_combate (
    id_accion INT AUTO_INCREMENT PRIMARY KEY,
    tipo_accion VARCHAR(80) NOT NULL,
    dano INT DEFAULT 0,
    descripcion TEXT,
    id_turno INT NOT NULL,
    CONSTRAINT fk_accion_turno FOREIGN KEY (id_turno) REFERENCES turno(id_turno) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT IGNORE INTO rol(nombre) VALUES
('Administrador'),
('Jugador'),
('Narrador');
"""


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_personajes', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql=SQL_CREATE_MISSING_TABLES,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
