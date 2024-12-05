from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil/', views.perfil, name='perfil'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('cinta/', views.cinta, name='cinta'),
    path('helecho/', views.helecho, name='helecho'),
    path('lirio/', views.lirio, name='lirio'),
    path('gerbera/', views.gerbera, name='gerbera'),
    path('ficus/', views.ficus, name='ficus'),
    path('palma/', views.palma, name='palma'),
    path('orqui/', views.orqui, name='orqui'),
    path('sanse/', views.sanse, name='sanse'),
    path('poto/', views.poto, name='poto'),
    path('aboutas/', views.aboutas, name='aboutas'),
]