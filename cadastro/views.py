from django.shortcuts import render
from django.contrib.auth.models import User
from .models import PessoaModel
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.http import HttpResponse


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass')
        
        user = auth.authenticate(username=username, password=password)

        if not user:
            return HttpResponse('Usuario Invalido!')
        
        auth.login( request, user)
        return redirect(reverse('profile'))

    return render(request, 'login.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass')
        User.objects.create_user(username=username,email=username, password=password)

        return redirect(reverse('login'))
    
    return render(request, 'signup.html')


def logout(request):
    request.session.flush()
    return redirect(reverse('login'))


def profile(request):

    return render(request, 'profile.html')
