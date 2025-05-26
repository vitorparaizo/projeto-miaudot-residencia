# forms.py
from django import forms
from .models import Pet  # importe seu modelo Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['foto', 'nome', 'descricao', 'idade', 'vacinado']  # campos que quer no form
