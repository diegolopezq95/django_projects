from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm

def index(request):
    return render(request,'index.html', {
        'message': 'Listado de productos',
        'title': 'Productos',
        'products': [
            {'title': 'Playera', 'price': 5, 'stock': True},
            {'title': 'Camisa', 'price': 4, 'stock': True},
            {'title': 'Mochila', 'price': 20, 'stock': False},
        ]
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user) #to generate session for an user
            print('User authenticated')
            messages.success(request, 'Welcome {}'.format(user.username))
            return redirect('index')
        else:


            messages.error(request, 'User or password not valid')
    return render(request, 'users/login.html', {

    })

def logout_view(request):
        logout(request)
        messages.success(request, 'session closed successfully')
        return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'User created successfully')
            return redirect('index')

    return render(request, 'users/register.html', {
        'form': form
    })
