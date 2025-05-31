from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import PetForm
from .models import Pet
from .models import Ong
from .models import Adocao
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required;


def home_view(request):
    pets = Pet.objects.all()
    return render(request, 'pages/home.html', {'pets': pets})

@login_required()
def petregister_view(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.ong = request.user
            pet.save()

            return redirect('petsCard')  
    else:
        form = PetForm()

    return render(request, 'pages/petRegister.html', {'form': form})


def petDescription_view(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pages/petDescription.html', {'pet':pet})


@login_required()
def petCard_view(request):
    pets = Pet.objects.all().order_by('-data_postagem')
    return render(request, 'pages/petsCard.html', {'pets': pets})

@login_required()
def pet_list_view(request):
    pets = Pet.objects.all()
    return render(request, 'pages/petsCard.html', {'pets': pets})

@login_required()
def petAdoptionForm_view(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        Adocao.objects.create(
            pet=pet,
            nome=nome,
            email=email,
            mensagem=mensagem
        )
        return render(request, 'pages/adoptionForm.html', {'pet': pet, 'sucesso': True})

    return render(request, 'pages/adoptionForm.html', {'pet':pet})


@login_required()
def petInfo_view(request):
    return render(request, 'pages/info.html')

@login_required()
def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'autenticacao/register.html', {'user_form': user_form})


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


def logout_view(request):
    logout(request)
    return redirect('login')
