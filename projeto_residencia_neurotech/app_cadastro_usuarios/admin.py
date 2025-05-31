from django.contrib import admin
from .models import Pet
from .models import Adocao

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'foto') 


admin.site.register(Adocao)