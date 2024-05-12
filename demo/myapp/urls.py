from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="inicio"),
    path("importar_ata/", views.importar_ata, name="importar_ata"),
    path("upload_file/", views.upload_file, name="upload_file"),
    path("emitir_historico/", views.emitir_historico, name="emitir_historico"),
    path("populate_and_download/", views.populate_and_download, name="populate_and_download"),
]