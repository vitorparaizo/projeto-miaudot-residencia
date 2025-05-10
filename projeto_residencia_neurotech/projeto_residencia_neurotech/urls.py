from django.urls import path 
from app_cadastro_usuarios import views
from app_cadastro_usuarios.views import login_view, register_view, inicio_view, logout_view
from django.contrib import admin

urlpatterns = [
    # rota , view , responsavel, nome 

    path('',views.home, name="home"),
    path('admin/', admin.site.urls),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),

    path('login/', login_view, name='login'),
    path('login/', logout_view, name='logout'),
    path('inicio/', inicio_view, name='inicio'),
    path('register/', register_view, name='register')

    
]

