# Portal D&D — Módulo de Usuarios y Autenticación

**Laboratorio de Software III · Avance No. 1 · GRUPO 1**  
Plataforma colaborativa para juegos de rol Dungeons & Dragons.

---

## Módulo implementado

**Usuarios y Autenticación** — gestión de usuarios con roles diferenciados:
- **Jugador**: acceso básico a la plataforma
- **Narrador**: gestión de partidas e historias
- **Administrador**: control total del sistema

### CRUDs entregados

| # | CRUD | Modelo | Operaciones |
|---|------|--------|-------------|
| 1 | Gestión de Aventureros | `User` + `PerfilUsuario` | Crear · Listar · Editar · Eliminar |
| 2 | Gestión de Roles | `Rol` | Crear · Listar · Editar · Eliminar |

---

## Requisitos previos

- Python **3.12**
- **XAMPP** (MySQL activo en puerto 3306)
- pip

---

## Cómo abrir el proyecto desde cero

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd dnd_auth
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
pip install django==6.0.4 mysqlclient
```

### 4. Configurar la base de datos en XAMPP

1. Abrir **XAMPP** → iniciar **Apache** y **MySQL**
2. Ir a `http://localhost/phpmyadmin`
3. Crear una base de datos llamada:

```
dnd_auth_db
```

> Collation recomendada: `utf8mb4_unicode_ci`

### 5. Aplicar migraciones

```bash
python manage.py migrate
```

### 6. (Opcional) Crear superusuario para el admin de Django

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

---

| Acción | URL |
|--------|-----|
| **Listar** todos los usuarios | `http://127.0.0.1:8000/usuarios/` |
| **Crear** nuevo usuario | `http://127.0.0.1:8000/usuarios/crear/` |
| **Editar** usuario (reemplazar `1` por el ID) | `http://127.0.0.1:8000/usuarios/1/editar/` |
| **Eliminar** usuario | `http://127.0.0.1:8000/usuarios/1/eliminar/` |


| Acción | URL |
|--------|-----|
| **Listar** todos los roles | `http://127.0.0.1:8000/usuarios/roles/` |
| **Crear** nuevo rol | `http://127.0.0.1:8000/usuarios/roles/crear/` |
| **Editar** rol | `http://127.0.0.1:8000/usuarios/roles/1/editar/` |
| **Eliminar** rol | `http://127.0.0.1:8000/usuarios/roles/1/eliminar/` |

| | URL |
|-|-----|
| Página principal (redirige automáticamente) | `http://127.0.0.1:8000/` |
| Panel de administración Django | `http://127.0.0.1:8000/admin/` |

---

## Stack tecnológico

| Componente | Tecnología |
|-----------|-----------|
| Backend | Django 6.0.4 (Python 3.12) |
| Base de datos | MySQL via XAMPP + mysqlclient |
| Frontend | Bootstrap 5 (CDN) + CSS personalizado |
| Autenticación | Sistema de auth nativo de Django |
| Control de versiones | Git |

---

## Flujo de demostración sugerido para la presentación

1. Mostrar la **lista de usuarios** vacía → `http://127.0.0.1:8000/usuarios/`
2. **Crear** un usuario con rol *Jugador*
3. **Crear** otro con rol *Narrador*
4. **Editar** uno de ellos y cambiarle el rol a *Administrador*
5. **Eliminar** un usuario (mostrar la confirmación)
6. Ir a **lista de roles** → `http://127.0.0.1:8000/usuarios/roles/`
7. **Crear** un rol personalizado (ej: "Guardián del Tesoro")
8. **Editar** el rol
9. **Eliminar** el rol (mostrar la confirmación)
