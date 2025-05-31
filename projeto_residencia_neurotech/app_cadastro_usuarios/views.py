from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import PetForm
from .models import Pet
from .models import Ong
from django.shortcuts import render, redirect, get_object_or_404;


def home_view(request):
    pets = Pet.objects.all()
    return render(request, 'pages/home.html', {'pets': pets})

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



def petCard_view(request):
    pets = Pet.objects.all().order_by('-data_postagem')
    return render(request, 'pages/petsCard.html', {'pets': pets})

def pet_list_view(request):
    pets = Pet.objects.all()
    return render(request, 'pages/petsCard.html', {'pets': pets})


def petAdoptionForm_view(request, pet_id):
    pet = get_object_or_404(request, pet_id)
    return render(request, 'pages/adoptionForm.html', {'pet':pet})


def petInfo_view(request):
    return render(request, 'pages/info.html')

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('inicio')
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
