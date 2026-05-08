from django.urls import path
from . import views

app_name = 'gestion_personajes'

urlpatterns = [

    # PERSONAJES
    path('', views.personaje_list, name='personaje_list'),
    path('crear/', views.personaje_create, name='personaje_create'),

    path('<int:pk>/', views.personaje_detail, name='personaje_detail'),
    path('<int:pk>/editar/', views.personaje_update, name='personaje_update'),
    path('<int:pk>/eliminar/', views.personaje_delete, name='personaje_delete'),

    # CLASES
    path('clases/', views.clase_list, name='clase_list'),
    path('clases/crear/', views.clase_create, name='clase_create'),
    path('clases/editar/<int:pk>/', views.clase_update, name='clase_update'),
    path('clases/eliminar/<int:pk>/', views.clase_delete, name='clase_delete'),

    # RAZAS
    path('razas/', views.lista_razas, name='lista_razas'),
    path('razas/crear/', views.crear_raza, name='crear_raza'),
    path('razas/editar/<int:id>/', views.editar_raza, name='editar_raza'),
    path('razas/eliminar/<int:id>/', views.eliminar_raza, name='eliminar_raza'),
]