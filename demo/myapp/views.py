from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.

def home(request):
    return render(request, "index.html")

def importar_ata(request):
    return render(request, "importar_ata.html")

def todos(request):
    items = TodoItem. objects.all()
    return render(request, "todos.html", {"todos": items})