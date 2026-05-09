# Portal D&D — Módulo de Usuarios y Gestión de Personajes

**Laboratorio de Software III · Avance No. 2 · GRUPO 1**  
Plataforma colaborativa para juegos de rol Dungeons & Dragons.

---

## Módulos implementados

### Módulo 1 — Usuarios y Roles
Gestión de usuarios con roles diferenciados:
- **Jugador**: acceso básico a la plataforma
- **Narrador**: gestión de partidas e historias
- **Administrador**: control total del sistema

### Módulo 2 — Gestión de Personajes
Creación y administración de personajes D&D con atributos completos, razas y clases.

### CRUDs entregados

| # | CRUD | Modelo | Operaciones |
|---|------|--------|-------------|
| 1 | Gestión de Aventureros | `User` + `PerfilUsuario` | Crear · Listar · Editar · Eliminar |
| 2 | Gestión de Roles | `Rol` | Crear · Listar · Editar · Eliminar |
| 3 | Gestión de Personajes | `Personaje` | Crear · Listar · Ver detalle · Editar · Eliminar |
| 4 | Gestión de Clases | `Clase` | Crear · Listar · Editar · Eliminar |
| 5 | Gestión de Razas | `Raza` | Crear · Listar · Editar · Eliminar |

---

## Requisitos previos

- Python **3.12+**
- **XAMPP** (MySQL/MariaDB activo en puerto 3306)
- pip

---

## Cómo abrir el proyecto desde cero

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd dnd-auth
```

### 2. Crear y activar el entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos en XAMPP

1. Abrir **XAMPP** → iniciar **Apache** y **MySQL**
2. Ir a `http://localhost/phpmyadmin`
3. Crear una base de datos con estos datos exactos:

| Campo | Valor |
|-------|-------|
| Nombre | `rpg_platform` |
| Cotejamiento | `utf8mb4_unicode_ci` |

> La configuración de conexión en `dnd_project/settings.py` usa:
> - Host: `127.0.0.1` · Puerto: `3306` · Usuario: `root` · Contraseña: *(vacía)*

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

Esto crea automáticamente todas las tablas necesarias:
- Tablas de Django (`auth_user`, `django_migrations`, etc.)
- Tablas de usuarios: `usuarios_rol`, `usuarios_perfilusuario`
- Tablas de personajes: `personaje`, `clase`, `raza`, `habilidad`, `personaje_habilidad`
- Tablas colaborativas: `campania`, `npc`, `mision`, `sesion`, `turno`, `combate`, y más

### 6. (Opcional) Crear superusuario para el admin de Django

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador: `http://127.0.0.1:8000/`

---

## URLs disponibles

### Usuarios

| Acción | URL |
|--------|-----|
| Listar todos los usuarios | `http://127.0.0.1:8000/usuarios/` |
| Crear nuevo usuario | `http://127.0.0.1:8000/usuarios/crear/` |
| Editar usuario | `http://127.0.0.1:8000/usuarios/<id>/editar/` |
| Eliminar usuario | `http://127.0.0.1:8000/usuarios/<id>/eliminar/` |
| Listar todos los roles | `http://127.0.0.1:8000/usuarios/roles/` |
| Crear nuevo rol | `http://127.0.0.1:8000/usuarios/roles/crear/` |
| Editar rol | `http://127.0.0.1:8000/usuarios/roles/<id>/editar/` |
| Eliminar rol | `http://127.0.0.1:8000/usuarios/roles/<id>/eliminar/` |

### Personajes

| Acción | URL |
|--------|-----|
| Listar todos los personajes | `http://127.0.0.1:8000/personajes/` |
| Crear nuevo personaje | `http://127.0.0.1:8000/personajes/crear/` |
| Ver detalle de personaje | `http://127.0.0.1:8000/personajes/<id>/` |
| Editar personaje | `http://127.0.0.1:8000/personajes/<id>/editar/` |
| Eliminar personaje | `http://127.0.0.1:8000/personajes/<id>/eliminar/` |
| Listar clases | `http://127.0.0.1:8000/personajes/clases/` |
| Crear clase | `http://127.0.0.1:8000/personajes/clases/crear/` |
| Editar clase | `http://127.0.0.1:8000/personajes/clases/editar/<id>/` |
| Eliminar clase | `http://127.0.0.1:8000/personajes/clases/eliminar/<id>/` |
| Listar razas | `http://127.0.0.1:8000/personajes/razas/` |
| Crear raza | `http://127.0.0.1:8000/personajes/razas/crear/` |
| Editar raza | `http://127.0.0.1:8000/personajes/razas/editar/<id>/` |
| Eliminar raza | `http://127.0.0.1:8000/personajes/razas/eliminar/<id>/` |

### General

| | URL |
|-|-----|
| Página principal (redirige a usuarios) | `http://127.0.0.1:8000/` |
| Panel de administración Django | `http://127.0.0.1:8000/admin/` |

---

## Stack tecnológico

| Componente | Tecnología |
|-----------|-----------|
| Backend | Django 6.0.4 (Python 3.12+) |
| Base de datos | MySQL/MariaDB via XAMPP + mysqlclient |
| Frontend | Bootstrap 5 (CDN) + CSS personalizado temático D&D |
| Autenticación | Sistema de auth nativo de Django |
| Control de versiones | Git |

---

## Flujo de demostración sugerido para la presentación

**Módulo Usuarios:**
1. Ir a `http://127.0.0.1:8000/usuarios/roles/` → crear los roles *Jugador*, *Narrador*, *Administrador*
2. Ir a `http://127.0.0.1:8000/usuarios/` → crear dos usuarios asignándoles roles distintos
3. Editar uno y cambiarle el rol
4. Mostrar la confirmación de eliminación

**Módulo Personajes:**
1. Ir a `http://127.0.0.1:8000/personajes/clases/` → crear clases (ej: *Guerrero*, *Mago*, *Pícaro*)
2. Ir a `http://127.0.0.1:8000/personajes/razas/` → crear razas (ej: *Humano*, *Elfo*, *Enano*)
3. Ir a `http://127.0.0.1:8000/personajes/crear/` → crear un personaje asignado a un usuario
4. Ver el detalle del personaje y sus atributos
5. Editar el personaje y mostrar el cambio

---

## Estructura del proyecto

```
dnd-auth/
├── dnd_project/          # Configuración global Django
│   ├── settings.py
│   └── urls.py
├── usuarios/             # App: gestión de usuarios y roles
│   ├── models.py         # Rol, PerfilUsuario
│   ├── views.py          # CRUDs de usuarios y roles
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── gestion_personajes/   # App: gestión de personajes D&D
│   ├── models.py         # Personaje, Clase, Raza, Habilidad
│   ├── views.py          # CRUDs de personajes, clases y razas
│   ├── forms.py
│   ├── urls.py
│   └── templates/
├── manage.py
└── requirements.txt
```
