from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.views.decorators.cache import cache_control

def inicio(request):
    return render(request, 'flor/inicio.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, '¡Cuenta creada con éxito! Por favor, inicia sesión.')
            return redirect('login')
        else:
            print(form.errors) 
            messages.error(request, 'Hubo un error al crear la cuenta. Por favor, verifica los datos e inténtalo nuevamente.')
    else:
        form = UserRegisterForm()
    return render(request, 'flor/register.html', {'form': form})
from .forms import CustomAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Por favor, revisa tus credenciales.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'flor/login.html', {'form': form})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    logout(request)
    messages.success(request, "¡Has cerrado sesión exitosamente!")
    return redirect('inicio')

def dashboard(request):
    return render(request, 'flor/dashboard.html', {'display_messages': True})

def perfil(request):
    plantas_favoritas = []
    return render(request, 'flor/perfil.html', {'plantas_favoritas': plantas_favoritas})

def ayuda(request):
    return render(request, 'flor/ayuda.html')

def cinta(request):
    return render(request, 'flor/cinta.html')

def helecho(request):
    return render(request, 'flor/helecho.html')

def lirio(request):
    return render(request, 'flor/lirio_de_la_paz.html')

def gerbera(request):
    return render(request, 'flor/gerberas.html')

def ficus(request):
    return render(request, 'flor/ficus_benjamina.html')

def palma(request):
    return render(request, 'flor/Palma_kentia.html')

def sanse(request):
    return render(request, 'flor/sanse.html')

def orqui(request):
    return render(request, 'flor/orqui.html')

def poto(request):
    return render(request, 'flor/poto.html')

def aboutas(request):
    return render(request, 'flor/aboutas.html')