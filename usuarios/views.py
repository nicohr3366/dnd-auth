from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import PerfilUsuario, Rol
from .forms import UsuarioCrearForm, UsuarioEditarForm, RolForm
from .models import Clase, Personaje, Raza
from .forms import ClaseForm, PersonajeForm, RazaForm


#USUARIOS

def usuarios_lista(request):
    usuarios = User.objects.select_related('perfil').all().order_by('username')
    return render(request, 'usuarios/usuarios/lista.html', {'usuarios': usuarios})


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


def usuario_eliminar(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        nombre = user.username
        user.delete()
        messages.success(request, f'Aventurero "{nombre}" eliminado.')
        return redirect('usuarios:lista')
    return render(request, 'usuarios/usuarios/eliminar.html', {'usuario': user})


# ROLES

def roles_lista(request):
    roles = Rol.objects.all().order_by('nombre')
    return render(request, 'usuarios/roles/lista.html', {'roles': roles})


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


def rol_eliminar(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        nombre = rol.nombre
        rol.delete()
        messages.success(request, f'Rol "{nombre}" eliminado.')
        return redirect('usuarios:roles_lista')
    return render(request, 'usuarios/roles/eliminar.html', {'rol': rol})


# ===== Gestion de personajes =====
# Clase
def clase_list(request):
	clases = Clase.objects.all()
	return render(request, 'gestion_personajes/clase_list.html', {'clases': clases})


def clase_create(request):
	if request.method == 'POST':
		form = ClaseForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Clase creada correctamente.')
			return redirect('gestion_personajes:clase_list')
	else:
		form = ClaseForm()
	return render(request, 'gestion_personajes/clase_form.html', {'form': form, 'title': 'Crear Clase'})


def clase_update(request, pk):
	clase = get_object_or_404(Clase, pk=pk)
	if request.method == 'POST':
		form = ClaseForm(request.POST, instance=clase)
		if form.is_valid():
			form.save()
			messages.success(request, 'Clase actualizada.')
			return redirect('gestion_personajes:clase_list')
	else:
		form = ClaseForm(instance=clase)
	return render(request, 'gestion_personajes/clase_form.html', {'form': form, 'title': 'Editar Clase'})


def clase_delete(request, pk):
	clase = get_object_or_404(Clase, pk=pk)
	if request.method == 'POST':
		clase.delete()
		messages.success(request, 'Clase eliminada.')
		return redirect('gestion_personajes:clase_list')
	return render(request, 'gestion_personajes/clase_confirm_delete.html', {'clase': clase})


# Personajes
def personaje_list(request):
	personajes = Personaje.objects.all()
	return render(request, 'crud_personajes/personaje_list.html', {'personajes': personajes})


def personaje_create(request):
	if request.method == 'POST':
		form = PersonajeForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Personaje creado correctamente.')
			return redirect('gestion_personajes:personaje_list')
	else:
		form = PersonajeForm()
	return render(request, 'crud_personajes/personaje_form.html', {'form': form, 'title': 'Crear Personaje'})


def personaje_update(request, pk):
	personaje = get_object_or_404(Personaje, pk=pk)
	if request.method == 'POST':
		form = PersonajeForm(request.POST, instance=personaje)
		if form.is_valid():
			form.save()
			messages.success(request, 'Personaje actualizado.')
			return redirect('gestion_personajes:personaje_list')
	else:
		form = PersonajeForm(instance=personaje)
	return render(request, 'crud_personajes/personaje_form.html', {'form': form, 'title': 'Editar Personaje'})


def personaje_delete(request, pk):
	personaje = get_object_or_404(Personaje, pk=pk)
	if request.method == 'POST':
		personaje.delete()
		messages.success(request, 'Personaje eliminado.')
		return redirect('gestion_personajes:personaje_list')
	return render(request, 'crud_personajes/personaje_confirm_delete.html', {'personaje': personaje})


def personaje_detail(request, pk):
	personaje = get_object_or_404(Personaje, pk=pk)
	return render(request, 'crud_personajes/personaje_detail.html', {'personaje': personaje})

# Razas

def lista_razas(request):
	razas = Raza.objects.all()
	return render(request, 'razas/lista.html', {'razas': razas})

def crear_raza(request):
	if request.method == 'POST':
		form = RazaForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'¡Raza "{form.cleaned_data["nombre"]}" creada exitosamente!')
			return redirect('gestion_personajes:lista_razas')
	else:
		form = RazaForm()
	return render(request, 'razas/crear.html', {'form': form})

def editar_raza(request, id):
	raza = get_object_or_404(Raza, id_raza=id)
	if request.method == 'POST':
		form = RazaForm(request.POST, instance=raza)
		if form.is_valid():
			form.save()
			messages.success(request, f'¡Raza "{raza.nombre}" actualizada correctamente!')
			return redirect('gestion_personajes:editar_razas')
	else:
		form = RazaForm(instance=raza)
	return render(request, 'razas/editar.html', {'form': form, 'raza': raza})

def eliminar_raza(request, id):
	raza = get_object_or_404(Raza, id_raza=id)
	if request.method == 'POST':
		nombre_raza = raza.nombre
		raza.delete()
		messages.success(request, f'¡Raza "{nombre_raza}" eliminada permanentemente!')
		return redirect('gestion_personajes:eliminar_razas')
	return render(request, 'razas/eliminar.html', {'raza': raza})