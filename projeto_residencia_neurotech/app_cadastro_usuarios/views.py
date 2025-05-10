from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('id_usuario')
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios.html', usuarios)

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('usuarios')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form':user_form})

    user_form = UserCreationForm()
    return render(request, 'login/register.html', {'user_form':user_form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login/register.html')
        else:
            login_form = AuthenticationForm
    else:  
        login_form = AuthenticationForm
        return render(request, 'login/login.html', {'login_form':login_form})



