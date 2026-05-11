from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Rol, PerfilUsuario
from .forms import PerfilForm, RolForm
from .decorators import solo_admin

# ─── LISTAR USUARIOS (lo ven todos) ─────────────────────
@login_required
def usuario_listar(request):
    usuarios = User.objects.all().select_related('perfil')   # ← CORREGIDO
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})

# ─── CREAR USUARIO (solo admin) ─────────────────────────
@login_required
@solo_admin
def usuario_crear(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado.')
            return redirect('usuarios:usuario_listar')
    else:
        form = PerfilForm()
    return render(request, 'usuarios/form.html', {'form': form, 'titulo': 'Crear Usuario'})

# ─── EDITAR USUARIO (solo admin, y solo él puede cambiar el rol) ───
@login_required
@solo_admin
def usuario_editar(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    perfil = get_object_or_404(PerfilUsuario, user=usuario)

    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            # Solo superusuario puede cambiar el rol
            if not request.user.is_superuser:
                messages.error(request, 'No tienes permiso para cambiar roles.')
                return redirect('usuarios:usuario_listar')
            form.save()
            messages.success(request, 'Usuario actualizado.')
            return redirect('usuarios:usuario_listar')
    else:
        form = PerfilForm(instance=perfil)

    if not request.user.is_superuser:
        form.fields['rol'].disabled = True

    return render(request, 'usuarios/form.html', {
        'form': form,
        'titulo': 'Editar Usuario',
        'es_admin': request.user.is_superuser
    })

# ─── ELIMINAR USUARIO (solo admin) ──────────────────────
@login_required
@solo_admin
def usuario_eliminar(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado.')
        return redirect('usuarios:usuario_listar')
    return render(request, 'usuarios/confirmar_eliminar.html', {'usuario': usuario})

# ─── ROLES (todo solo admin) ────────────────────────────
@login_required
@solo_admin
def rol_listar(request):
    roles = Rol.objects.all()
    return render(request, 'usuarios/roles_listar.html', {'roles': roles})

@login_required
@solo_admin
def rol_crear(request):
    form = RolForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Rol creado.')
        return redirect('usuarios:rol_listar')
    return render(request, 'usuarios/roles_form.html', {'form': form, 'titulo': 'Crear Rol'})

@login_required
@solo_admin
def rol_editar(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    form = RolForm(request.POST or None, instance=rol)
    if form.is_valid():
        form.save()
        messages.success(request, 'Rol actualizado.')
        return redirect('usuarios:rol_listar')
    return render(request, 'usuarios/roles_form.html', {'form': form, 'titulo': 'Editar Rol'})

@login_required
@solo_admin
def rol_eliminar(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        rol.delete()
        messages.success(request, 'Rol eliminado.')
        return redirect('usuarios:rol_listar')
    return render(request, 'usuarios/roles_confirmar_eliminar.html', {'rol': rol})