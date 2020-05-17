from django.shortcuts import render
from .models import Post

# Create your views here.

def hello_blog(request):
    lista = [
        'Django', 
        'Python', 
        'Html', 
        'Banco de dados'
    ]
    list_posts = Post.objects.all()
    
    data = {
        'name': 'Django 3',
        'lista_tecnologias': lista,
        'posts': list_posts}
    
    
    return render(request, 'index.html', data)
