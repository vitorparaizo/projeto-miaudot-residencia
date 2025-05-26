# models.py
from django.db import models
from django.contrib.auth.models import User

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
