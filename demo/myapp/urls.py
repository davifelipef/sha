from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("importar_ata.html", views.importar_ata, name="importar_ata"),
    path("todos/", views.todos, name="Todos")
]