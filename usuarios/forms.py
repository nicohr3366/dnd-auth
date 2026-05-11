from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario, Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PerfilForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False, label="Confirmar contraseña")

    class Meta:
        model = PerfilUsuario
        fields = ['rol']  # solo el campo rol del perfil
        widgets = {
            'rol': forms.Select(attrs={'class': 'form-control'}, choices=PerfilUsuario.ROL_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.usuario_id:
            self.fields['username'].initial = self.instance.usuario.username
            self.fields['email'].initial = self.instance.usuario.email
            self.fields['password'].required = False
            self.fields['password_confirm'].required = False
        else:
            self.fields['password'].required = True
            self.fields['password_confirm'].required = True

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if self.instance.pk:
            # Editar perfil existente
            user = self.instance.usuario
            user.username = username
            user.email = email
            if password:
                user.set_password(password)
            if commit:
                user.save()
        else:
            # Crear nuevo usuario y perfil
            user = User.objects.create_user(username=username, email=email, password=password)
            self.instance.usuario = user

        if commit:
            self.instance.save()
        return self.instance