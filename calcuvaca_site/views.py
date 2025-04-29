from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def home(request: HttpRequest):
    context = {'message': 'Hola, Mundo!'}

    return render(request, 'home.html', context)
