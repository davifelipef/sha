from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="inicio"),
    path("importar_ata/", views.importar_ata, name="importar_ata"),
    path("todos/", views.todos, name="Todos")
]