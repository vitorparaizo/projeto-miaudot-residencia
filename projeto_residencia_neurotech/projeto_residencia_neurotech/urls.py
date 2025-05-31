from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app_cadastro_usuarios.views import (
    login_view, register_view, home_view, logout_view,
    petregister_view, petDescription_view, petCard_view,
    petAdoptionForm_view, petInfo_view
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='inicio'),
    
    path('pet/register/', petregister_view, name="petregister"),
    path('pet/description/', petDescription_view, name="petDescription"),
    path('pet/list/', petCard_view, name='petsCard'),
    path('pet/adoption-form/', petAdoptionForm_view, name="petAdoptionForm"),
    path('pet/info/', petInfo_view, name='info'),
    
    path('register/', register_view, name='register'),
    path('pet/<int:pet_id>/adoption-form/', petAdoptionForm_view, name="petAdoptionForm"),
    path('pet/description/<int:pet_id>/', petDescription_view, name="petDescription"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
