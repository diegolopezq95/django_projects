from django.http import HttpResponse
from django.shortcuts import render

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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password')

        print('username')
        print('password')
    return render(request, 'users/login.html', {

    })
