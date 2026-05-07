from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # Usuarios
    path('', views.usuarios_lista, name='lista'),
    path('crear/', views.usuario_crear, name='crear'),
    path('registro/', views.usuario_crear, name='registro'),
    path('<int:pk>/editar/', views.usuario_editar, name='editar'),
    path('<int:pk>/eliminar/', views.usuario_eliminar, name='eliminar'),
    # Roles
    path('roles/', views.roles_lista, name='roles_lista'),
    path('roles/crear/', views.rol_crear, name='rol_crear'),
    path('roles/<int:pk>/editar/', views.rol_editar, name='rol_editar'),
    path('roles/<int:pk>/eliminar/', views.rol_eliminar, name='rol_eliminar'),

    # === Gestion de personajes
    # URLs para Clases
        path('', views.clase_list, name='clase_list'),
    path('crear/', views.clase_create, name='clase_create'),
    path('editar/<int:pk>/', views.clase_update, name='clase_update'),
    path('eliminar/<int:pk>/', views.clase_delete, name='clase_delete'),
    
    # URLs para Personajes
    path('personajes/', views.personaje_list, name='personaje_list'),
    path('personajes/crear/', views.personaje_create, name='personaje_create'),
    path('personajes/<int:pk>/', views.personaje_detail, name='personaje_detail'),
    path('personajes/<int:pk>/editar/', views.personaje_update, name='personaje_update'),
    path('personajes/<int:pk>/eliminar/', views.personaje_delete, name='personaje_delete'),

    # URLs para Razas
    path('razas/', views.lista_razas, name='lista_razas'),
    path('razas/crear/', views.crear_raza, name='crear_raza'),
    path('razas/editar/<int:id>/', views.editar_raza, name='editar_raza'),
    path('razas/eliminar/<int:id>/', views.eliminar_raza, name='eliminar_raza'),
]
