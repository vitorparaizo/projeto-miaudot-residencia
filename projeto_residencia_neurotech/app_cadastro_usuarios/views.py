from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def home_view(request):
    return render(request, 'pages/home.html')

def petregister_view(request):
    return render(request, 'pages/petregister.html')

def petDescription_view(request):
    return render(request, 'pages/petDescription.html')

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('inicio')
    else:
        user_form = UserCreationForm()
    return render(request, 'autenticacao/register.html', {'user_form':user_form})

    user_form = UserCreationForm()

    return render(request, 'autenticacao/register.html', {'user_form':user_form})

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
        return render(request, 'autenticacao/login.html', {'login_form':login_form})


def logout_view(request):
    logout(request)
    return redirect('login')




