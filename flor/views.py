from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login

def inicio(request):
    return render(request, 'flor/inicio.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrige los errores.')
    else:
        form = UserRegisterForm()
    return render(request, 'flor/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Por favor, revisa tus credenciales.')
    else:
        form = AuthenticationForm()

    return render(request, 'flor/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'flor/dashboard.html')

def perfil(request):
    plantas_favoritas = []
    return render(request, 'perfil.html', {'plantas_favoritas': plantas_favoritas})

def ayuda(request):
    return render(request, 'flor/ayuda.html')