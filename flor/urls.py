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
]