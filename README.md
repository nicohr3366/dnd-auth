# Portal D&D — Usuarios y Gestión de Personajes

**Laboratorio de Software III · Avance No. 2 · GRUPO 1**

---

## CRUDs entregados

| # | CRUD | Acceso |
|---|------|--------|
| 1 | Gestión de Aventureros (`User` + `PerfilUsuario`) | Solo Administrador |
| 2 | Gestión de Roles (`Rol`) | Todos los usuarios |
| 3 | Gestión de Personajes (`Personaje`) | Todos los usuarios |
| 4 | Gestión de Clases (`Clase`) | Todos los usuarios |
| 5 | Gestión de Razas (`Raza`) | Todos los usuarios |

Operaciones en cada CRUD: Crear · Listar · Ver detalle · Editar · Eliminar

> Modelos adicionales en BD sin CRUD propio: `Habilidad`, `PersonajeHabilidad`, `SolicitudEdicionRol`.

---

## Requisitos

- Python **3.12+** · **XAMPP** (MySQL en puerto 3306) · pip

---

## Instalación

```bash
# 1. Clonar
git clone <URL_DEL_REPOSITORIO>
cd dnd-auth

# 2. Entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Dependencias
pip install -r requirements.txt
```

---

## Configurar la base de datos (XAMPP)

> Conexión en `dnd_project/settings.py`: host `127.0.0.1`, puerto `3306`, usuario `root`, contraseña vacía.

### Opción A — Importar el SQL exportado (recomendado)

Restaura todas las tablas con los datos existentes. **No necesitas correr migraciones después.**

1. Inicia **Apache** y **MySQL** en XAMPP
2. Ve a `http://localhost/phpmyadmin`
3. Crea la base de datos: nombre `rpg_platform`, cotejamiento `utf8mb4_unicode_ci`
4. Selecciona `rpg_platform` → pestaña **Importar** → elige `database_export.sql` → **Continuar**

### Opción B — Base de datos vacía

1. Crea la base de datos `rpg_platform` en phpMyAdmin (mismo cotejamiento)
2. Ejecuta las migraciones:

```bash
python manage.py migrate
```

---

## Ejecutar

```bash
# (Opcional) Crear superusuario si la BD está vacía
python manage.py createsuperuser

python manage.py runserver
```

Abre `http://127.0.0.1:8000/` — redirige al dashboard o al login si no hay sesión.

---

## Permisos por rol

- **Cualquier usuario logueado**: ver usuarios, gestionar roles (excepto el rol "Administrador"), CRUD completo de personajes, clases y razas, ver y editar su perfil.
- **Administrador** (o superuser): además puede crear, editar y eliminar usuarios, y gestionar el rol "Administrador".
- **Registro público** (`/usuarios/registro/`): no permite elegir el rol "Administrador".

---

## URLs principales

| Sección | URL |
|---------|-----|
| Login / Logout / Registro | `/usuarios/login/` · `/usuarios/logout/` · `/usuarios/registro/` |
| Dashboard | `/usuarios/dashboard/` |
| Mi perfil / Editar | `/usuarios/perfil/` · `/usuarios/perfil/editar/` |
| Lista de usuarios | `/usuarios/` |
| Detalle / Crear / Editar / Eliminar usuario | `/usuarios/<id>/` · `/usuarios/crear/` · `/usuarios/<id>/editar/` · `/usuarios/<id>/eliminar/` |
| Dashboard admin de usuarios | `/usuarios/usuarios-dashboard/` |
| Roles | `/usuarios/roles/` (crear: `/roles/crear/`) |
| Personajes | `/personajes/` · `/personajes/inicio/` (dashboard) |
| Clases | `/personajes/clases/` |
| Razas | `/personajes/razas/` |
| Admin Django | `/admin/` |

---

## Stack

| Componente | Tecnología |
|-----------|-----------|
| Backend | Django 6.0.4 + Python 3.12+ |
| Base de datos | MySQL/MariaDB 10.6 via XAMPP + mysqlclient |
| Frontend | Bootstrap 5 (CDN) + CSS temático D&D |
| Auth | Django auth nativo + perfiles personalizados |

---

## Problemas comunes

- **`Can't connect to MySQL server`** — verifica que MySQL esté corriendo en XAMPP (puerto 3306)
- **`Unknown database 'rpg_platform'`** — crea la BD en phpMyAdmin con ese nombre exacto
- **`No module named 'MySQLdb'`** — ejecuta `pip install mysqlclient`
- **SQL no sube en phpMyAdmin** — aumenta `upload_max_filesize` y `post_max_size` a `64M` en `C:\xampp\php\php.ini` y reinicia Apache

---

## Estructura del proyecto

```
dnd-auth/
├── dnd_project/          # Configuración global (settings, urls)
├── usuarios/             # App: auth, usuarios, roles
│   ├── models.py         # Rol, PerfilUsuario, SolicitudEdicionRol
│   ├── views.py
│   ├── migrations/       # 3 migraciones
│   └── templates/
├── gestion_personajes/   # App: personajes, clases, razas
│   ├── models.py         # Personaje, Clase, Raza, Habilidad, PersonajeHabilidad
│   ├── views.py
│   ├── migrations/       # 3 migraciones
│   └── templates/
├── database_export.sql   # Dump completo de la BD (MariaDB 10.6)
├── manage.py
└── requirements.txt
```
