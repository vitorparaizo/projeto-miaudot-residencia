from django.urls import path 
from app_cadastro_usuarios import views

urlpatterns = [
    # rota , view , responsavel, nome 

    path('',views.home, name="home"),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
    
]
