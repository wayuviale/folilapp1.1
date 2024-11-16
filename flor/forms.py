from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    username = forms.CharField(
        label="Nombre",
        max_length=150,
        help_text="Solo 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_"
    )
    password1 = forms.CharField(
        label="Contraseña", 
        widget=forms.PasswordInput,
        help_text="Tu contraseña debe contener al menos 8 caracteres y no puede ser común o completamente numérica."
    )
    password2 = forms.CharField(
        label="Confirmación de Contraseña", 
        widget=forms.PasswordInput,
        help_text="Introduce la misma contraseña para verificación."
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']