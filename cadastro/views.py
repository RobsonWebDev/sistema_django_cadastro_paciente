from django.shortcuts import render
from django.contrib.auth.models import User
from .models import PessoaModel
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.http import HttpResponse
from django.contrib import messages


def login(request):

    context = {
        'titulo': 'Login',
        'mensagens':{
            'erro': 'Email/Senha Inválidos!'
        }
    }

    if request.method == 'GET':
        return render(request, 'login.html', context)
    
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass')
        
        user = auth.authenticate(username=username, password=password)

        if not user:
            return redirect(reverse('login'))
        
        auth.login( request, user)
        return redirect(reverse('profile'))
    

    return render(request, 'login.html', context)


def signup(request):

    context = {
        'titulo': 'Cadastro',
        'mensagens':{
            'sucesso': "Usuário cadastrado com sucesso!",
            'erro': 'Digite um email valido!'
        }
    }

    if request.method == 'GET':
        return render(request, 'signup.html', context)
    
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass')
        user = User.objects.create_user(username=username,email=username, password=password)

        if user.is_exist():
            return redirect(reverse('login'))

        return redirect(reverse('login'))
    
    return render(request, 'signup.html', context)


def logout(request):
    request.session.flush()
    return redirect(reverse('login'))


def profile(request):

    return render(request, 'profile.html')
