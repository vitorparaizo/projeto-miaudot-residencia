
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    idade = models.PositiveIntegerField()
    vacinado = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    foto = models.ImageField(upload_to='fotos_pets/')
    data_postagem = models.DateTimeField(auto_now_add=True)
    ong = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Curtida(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

class CandidaturaAdocao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

class Ong(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    endereco = models.CharField(max_length=255)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ongs')

    def __str__(self):
        return self.nome
