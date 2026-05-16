from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import PortalAuthenticationForm

app_name = 'usuarios'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/auth/login.html',
        authentication_form=PortalAuthenticationForm,
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='usuarios:login'), name='logout'),
    path('registro/', views.registro, name='registro_publico'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('perfil/editar/', views.editar_perfil_propio, name='editar_perfil'),
    # Usuarios
    path('', views.usuarios_lista, name='lista'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usuarios-dashboard/', views.usuarios_dashboard, name='usuarios_dashboard'),
    path('<int:pk>/', views.usuario_detalle, name='detalle'),
    path('crear/', views.usuario_crear, name='crear'),
    path('<int:pk>/editar/', views.usuario_editar, name='editar'),
    path('<int:pk>/eliminar/', views.usuario_eliminar, name='eliminar'),
    # Roles
    path('roles/', views.roles_lista, name='roles_lista'),
    path('roles/crear/', views.rol_crear, name='rol_crear'),
    path('roles/<int:pk>/editar/', views.rol_editar, name='rol_editar'),
    path('roles/<int:pk>/eliminar/', views.rol_eliminar, name='rol_eliminar'),
]
