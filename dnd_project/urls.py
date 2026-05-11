from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Página de inicio redirige a lista de usuarios
    path('', RedirectView.as_view(url='/usuarios/', permanent=False), name='home'),
    # Las URLs de usuarios con namespace
    path('usuarios/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    # Alias para usuaris (por si alguna plantilla lo llama así)
    path('usuaris/', include(('usuarios.urls', 'usuarios'), namespace='usuaris')),
    # ¡NUEVO! URLs de autenticación (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
]