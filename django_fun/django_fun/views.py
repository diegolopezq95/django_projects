from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html', {
    'message': 'Hola mundo desde la vista',
    'title': 'Titulo'
    })
