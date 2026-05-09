from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    # Usuarios
    path('', views.usuarios_lista, name='lista'),
    path('dashboard/', views.usuarios_dashboard, name='dashboard'),
    path('<int:pk>/', views.usuario_detalle, name='detalle'),
    path('crear/', views.usuario_crear, name='crear'),
    path('registro/', views.usuario_crear, name='registro'),
    path('<int:pk>/editar/', views.usuario_editar, name='editar'),
    path('<int:pk>/eliminar/', views.usuario_eliminar, name='eliminar'),
    # Roles
    path('roles/', views.roles_lista, name='roles_lista'),
    path('roles/crear/', views.rol_crear, name='rol_crear'),
    path('roles/<int:pk>/editar/', views.rol_editar, name='rol_editar'),
    path('roles/<int:pk>/eliminar/', views.rol_eliminar, name='rol_eliminar'),
]
