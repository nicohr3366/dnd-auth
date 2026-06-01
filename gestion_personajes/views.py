from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Clase, Personaje, Raza
from .forms import ClaseForm, PersonajeForm, RazaForm


@login_required
def clase_list(request):
    clases = Clase.objects.all()
    return render(request, 'gestion_personajes/clase_list.html', {'clases': clases})


@login_required
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


@login_required
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


@login_required
def clase_delete(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    if request.method == 'POST':
        clase.delete()
        messages.success(request, 'Clase eliminada.')
        return redirect('gestion_personajes:clase_list')
    return render(request, 'gestion_personajes/clase_confirm_delete.html', {'clase': clase})


# ========================
# VISTAS PARA PERSONAJES
# ========================

@login_required
def personaje_list(request):
    personajes = Personaje.objects.all()
    return render(request, 'crud_personajes/personaje_list.html', {'personajes': personajes})


@login_required
def personaje_create(request):
    if request.method == 'POST':
        form = PersonajeForm(request.POST)
        if form.is_valid():
            personaje = form.save(commit=False)
            personaje.user = request.user
            personaje.save()
            messages.success(request, 'Personaje creado correctamente.')
            return redirect('gestion_personajes:personaje_list')
    else:
        form = PersonajeForm()
    return render(request, 'crud_personajes/personaje_form.html', {'form': form, 'title': 'Crear Personaje'})


@login_required
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


@login_required
def personaje_delete(request, pk):
    personaje = get_object_or_404(Personaje, pk=pk)
    if request.method == 'POST':
        personaje.delete()
        messages.success(request, 'Personaje eliminado.')
        return redirect('gestion_personajes:personaje_list')
    return render(request, 'crud_personajes/personaje_confirm_delete.html', {'personaje': personaje})


@login_required
def personaje_detail(request, pk):
    personaje = get_object_or_404(Personaje, pk=pk)
    perfil = getattr(personaje.user, 'perfil', None)
    rol_nombre = perfil.rol.nombre if (perfil and perfil.rol) else 'Sin rol'
    return render(request, 'crud_personajes/personaje_detail.html', {
        'personaje': personaje,
        'rol_nombre': rol_nombre,
    })


@login_required
def dashboard(request):
    user = request.user

    # Rol del usuario (si existe perfil)
    perfil = getattr(user, 'perfil', None)
    rol_nombre = perfil.rol.nombre if (perfil and perfil.rol) else 'Sin rol'

    # Personajes del usuario
    user_personajes = Personaje.objects.filter(user=user)
    total_personajes = user_personajes.count()

    # Estadísticas globales: clases y razas
    clases = Clase.objects.all()
    razas = Raza.objects.all()

    # Contadores por clase y por raza
    class_stats = []
    for c in clases:
        cnt = Personaje.objects.filter(clase=c).count()
        class_stats.append({'nombre': c.nombre, 'count': cnt})

    raza_stats = []
    for r in razas:
        cnt = Personaje.objects.filter(raza=r).count()
        raza_stats.append({'nombre': r.nombre, 'count': cnt})

    context = {
        'rol_nombre': rol_nombre,
        'user_personajes': user_personajes,
        'total_personajes': total_personajes,
        'class_stats': class_stats,
        'raza_stats': raza_stats,
    }
    return render(request, 'crud_personajes/dashboard.html', context)

# ====== RAZAS ======

@login_required
def lista_razas(request):
    razas = Raza.objects.all()
    return render(request, 'razas/lista.html', {'razas': razas})

@login_required
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

@login_required
def editar_raza(request, id):
    raza = get_object_or_404(Raza, id_raza=id)
    if request.method == 'POST':
        form = RazaForm(request.POST, instance=raza)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡Raza "{raza.nombre}" actualizada correctamente!')
            return redirect('gestion_personajes:lista_razas')
    else:
        form = RazaForm(instance=raza)
    return render(request, 'razas/editar.html', {'form': form, 'raza': raza})

@login_required
def eliminar_raza(request, id):
    raza = get_object_or_404(Raza, id_raza=id)
    if request.method == 'POST':
        nombre_raza = raza.nombre
        raza.delete()
        messages.success(request, f'¡Raza "{nombre_raza}" eliminada permanentemente!')
        return redirect('gestion_personajes:lista_razas')
    return render(request, 'razas/eliminar.html', {'raza': raza})
