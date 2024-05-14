from django.test import TestCase
from django.core.files.uploadedfile import UploadedFile
from .views import importar_ata, processar_e_salvar_dados, validate_csv

class PagesResponse(TestCase):

    def test_base_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    