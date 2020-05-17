from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_blog(request):
    lista = ['Django', 'Python', 'Html', 'Banco de dados']
    data = {'name': 'Django 3', 'lista_tecnologias': lista}
    return render(request, 'index.html', data)
