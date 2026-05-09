from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Rol


class UsuarioCrearForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: aventurero_42'}),
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
    )
    rol = forms.ModelChoiceField(
        queryset=Rol.objects.all(),
        label='Rol',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    confirmar_password = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar = cleaned_data.get('confirmar_password')
        if password and confirmar and password != confirmar:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data


class UsuarioEditarForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    rol = forms.ModelChoiceField(
        queryset=Rol.objects.all(),
        label='Rol',
        empty_label='Dejar vacío para no cambiar',
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    password = forms.CharField(
        label='Nueva contraseña (opcional)',
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Dejar vacío para no cambiar'}),
    )

    def __init__(self, *args, **kwargs):
        self.usuario_id = kwargs.pop('usuario_id', None)
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if self.usuario_id:
            qs = qs.exclude(pk=self.usuario_id)
        if qs.exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso.')
        return username


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre del rol',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Guardián del Tesoro',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe los permisos y responsabilidades de este rol...',
            }),
        }


class PortalAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu usuario',
            'autofocus': True,
        }),
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu contraseña',
        }),
    )
