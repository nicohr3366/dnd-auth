from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.usuario_listar, name='usuario_listar'),
    path('crear/', views.usuario_crear, name='usuario_crear'),
    path('<int:pk>/editar/', views.usuario_editar, name='usuario_editar'),
    path('<int:pk>/eliminar/', views.usuario_eliminar, name='usuario_eliminar'),
    path('roles/', views.rol_listar, name='rol_listar'),
    path('roles/crear/', views.rol_crear, name='rol_crear'),
    path('roles/<int:pk>/editar/', views.rol_editar, name='rol_editar'),
    path('roles/<int:pk>/eliminar/', views.rol_eliminar, name='rol_eliminar'),
]