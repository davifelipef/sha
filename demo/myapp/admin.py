from django.contrib import admin
from .models import AtaResultados
from .models import TodoItem

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(AtaResultados)
