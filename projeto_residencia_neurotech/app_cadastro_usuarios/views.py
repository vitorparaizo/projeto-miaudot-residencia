from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import PetForm
from .models import Pet

# HOME VIEW (feed de pets ordenado do mais recente para o mais antigo)
def home_view(request):
    pets = Pet.objects.all()
    return render(request, 'pages/home.html', {'pets': pets})

# CADASTRO DE PET
def petregister_view(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # nome da url em urls.py
    else:
        form = PetForm()
    return render(request, 'pages/petregister.html', {'form': form})

# DESCRIÇÃO DO PET (página estática ou complementar)
def petDescription_view(request):
    return render(request, 'pages/petDescription.html')

# LISTAGEM DE PETS NO FORMATO CARD
def petCard_view(request):
    pets = Pet.objects.all().order_by('-data_postagem')
    return render(request, 'pages/petsCard.html', {'pets': pets})

# FORMULÁRIO DE ADOÇÃO
def petAdoptionForm_view(request):
    return render(request, 'pages/adoptionForm.html')

# PÁGINA DE INFORMAÇÕES
def petInfo_view(request):
    return render(request, 'pages/info.html')

# REGISTRO DE USUÁRIO
def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('inicio')
    else:
        user_form = UserCreationForm()
    return render(request, 'autenticacao/register.html', {'user_form': user_form})

# LOGIN DE USUÁRIO
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            login_form = AuthenticationForm()
            return render(request, 'autenticacao/login.html', {'login_form': login_form})
    else:  
        login_form = AuthenticationForm()
        return render(request, 'autenticacao/login.html', {'login_form': login_form})

# LOGOUT DE USUÁRIO
def logout_view(request):
    logout(request)
    return redirect('login')
