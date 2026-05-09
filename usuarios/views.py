from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import DatabaseError
from django.shortcuts import get_object_or_404, redirect, render

from gestion_personajes.models import Clase, Personaje, Raza

from .forms import RolForm, UsuarioCrearForm, UsuarioEditarForm
from .models import PerfilUsuario, Rol


def registro(request):
    if request.user.is_authenticated:
        return redirect('usuarios:dashboard')
    if request.method == 'POST':
        form = UsuarioCrearForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            rol = form.cleaned_data['rol']
            PerfilUsuario.objects.create(usuario=user, rol=rol)
            messages.success(request, f'Cuenta creada. Ya puedes iniciar sesión, {user.username}.')
            return redirect('usuarios:login')
    else:
        form = UsuarioCrearForm()
    form.fields['rol'].queryset = Rol.objects.exclude(nombre='Administrador')
    return render(request, 'usuarios/auth/registro.html', {'form': form})


@login_required
def dashboard(request):
    def safe_count(model):
        try:
            return model.objects.count()
        except DatabaseError:
            return 0

    rol_actual = 'Sin rol'
    try:
        perfil = request.user.perfil
    except (DatabaseError, AttributeError):
        perfil = None
    if perfil and perfil.rol:
        rol_actual = perfil.rol.nombre
    elif request.user.is_superuser:
        rol_actual = 'Administrador'
    contexto = {
        'total_usuarios': safe_count(User),
        'total_roles': safe_count(Rol),
        'total_clases': safe_count(Clase),
        'total_razas': safe_count(Raza),
        'total_personajes': safe_count(Personaje),
        'rol_actual': rol_actual,
    }
    return render(request, 'usuarios/dashboard.html', contexto)


@login_required
def usuarios_lista(request):
    usuarios = User.objects.select_related('perfil').all().order_by('username')
    return render(request, 'usuarios/usuarios/lista.html', {'usuarios': usuarios})


@login_required
def usuario_crear(request):
    if request.method == 'POST':
        form = UsuarioCrearForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            PerfilUsuario.objects.create(
                usuario=user,
                rol=form.cleaned_data['rol'],
            )
            messages.success(request, f'Aventurero "{user.username}" registrado exitosamente.')
            return redirect('usuarios:lista')
    else:
        form = UsuarioCrearForm()
    return render(request, 'usuarios/usuarios/crear.html', {'form': form})


@login_required
def usuario_editar(request, pk):
    user = get_object_or_404(User, pk=pk)
    perfil, _ = PerfilUsuario.objects.get_or_create(usuario=user)

    if request.method == 'POST':
        form = UsuarioEditarForm(request.POST, usuario_id=pk)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()
            if form.cleaned_data['rol']:
                perfil.rol = form.cleaned_data['rol']
                perfil.save()
            messages.success(request, f'Aventurero "{user.username}" actualizado correctamente.')
            return redirect('usuarios:lista')
    else:
        form = UsuarioEditarForm(
            initial={
                'username': user.username,
                'email': user.email,
                'rol': perfil.rol,
            },
            usuario_id=pk,
        )
    return render(request, 'usuarios/usuarios/editar.html', {'form': form, 'usuario': user})


@login_required
def usuario_eliminar(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        nombre = user.username
        user.delete()
        messages.success(request, f'Aventurero "{nombre}" eliminado.')
        return redirect('usuarios:lista')
    return render(request, 'usuarios/usuarios/eliminar.html', {'usuario': user})


@login_required
def roles_lista(request):
    roles = Rol.objects.all().order_by('nombre')
    return render(request, 'usuarios/roles/lista.html', {'roles': roles})


@login_required
def rol_crear(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            rol = form.save()
            messages.success(request, f'Rol "{rol.nombre}" creado exitosamente.')
            return redirect('usuarios:roles_lista')
    else:
        form = RolForm()
    return render(request, 'usuarios/roles/crear.html', {'form': form})


@login_required
def rol_editar(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            messages.success(request, f'Rol "{rol.nombre}" actualizado correctamente.')
            return redirect('usuarios:roles_lista')
    else:
        form = RolForm(instance=rol)
    return render(request, 'usuarios/roles/editar.html', {'form': form, 'rol': rol})


@login_required
def rol_eliminar(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        nombre = rol.nombre
        rol.delete()
        messages.success(request, f'Rol "{nombre}" eliminado.')
        return redirect('usuarios:roles_lista')
    return render(request, 'usuarios/roles/eliminar.html', {'rol': rol})
