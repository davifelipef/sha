from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class AtaResultados(models.Model):
    turma = models.CharField(max_length=100)
    serie = models.CharField(max_length=50)
    ano = models.IntegerField()
    aluno = models.CharField(max_length=300)
    nt_art = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Arte')
    nt_bio = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Biologia')
    nt_edf = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Ed. Física')
    nt_fil = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Filosofia')
    nt_fis = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Física')
    nt_geo = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Geografia')
    nt_his = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='História')
    nt_lin = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='L. Inglesa')
    nt_lpt = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='L. Portuguesa')
    nt_mat = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Matemática')
    nt_pro = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Projeto de Vida')
    nt_qui = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Química')
    nt_soc = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Sociologia')
    nt_tec = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]|S/N|EP|ES$', 'Nota inválida')], verbose_name='Tecnologia')

    def __str__(self):
        return self.name
    
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)