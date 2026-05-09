from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Clase, Personaje, Raza
from .forms import ClaseForm, PersonajeForm, RazaForm


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


# ========================
# VISTAS PARA PERSONAJES
# ========================

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

# ====== RAZAS ======

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