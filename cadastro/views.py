from django.shortcuts import render
from django.contrib.auth.models import User
from .models import PessoaModel


def login(request):
    pass

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass')
        User.objects.create_user(username=username,email=username, password=password)

    return render(request, 'index.html')