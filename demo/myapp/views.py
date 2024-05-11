from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db.models import Q
from .models import AtaResultados

# Create your views here.

def home(request):
    return render(request, "index.html")

def validate_csv(uploaded_file):
    # Validar se o arquivo é um CSV
    if not uploaded_file.name.endswith('.csv'):
        raise ValidationError('Apenas arquivos CSV são permitidos.')

def importar_ata(request):
    if request.method == 'POST':
        # Obter o arquivo CSV enviado
        uploaded_file = request.FILES.get('filename')  

        # Validar o arquivo CSV (se enviado)
        if uploaded_file:
            try:
                validate_csv(uploaded_file)
                # Processar e salvar os dados no banco de dados
                processar_e_salvar_dados(uploaded_file) 
                # Exibir mensagem de confirmação
                messages.success(request, 'Ata importada com sucesso!')
                # Limpar o campo de envio de arquivo
                return redirect('importar_ata')
            except ValidationError as e:
                messages.error(request, e.message)
                return render(request, 'importar_ata.html')
    return render(request, 'importar_ata.html')

@transaction.atomic
def processar_e_salvar_dados(uploaded_file):
    # Dedodificação e leitura do arquivo enviado por upload
    decoded_file = uploaded_file.read().decode('utf-8').splitlines()

    # Declaração das variáveis ano, turma e série
    i_ano = ""
    i_turma = ""
    i_serie = ""

    for line_index, line in enumerate(decoded_file):  
        # Pula as linhas vazias
        if not line.strip():
            continue
        
        # Especifica que a separação dos dados é feita pelo ponto e vírgula
        row_data = line.split(';')

        # Check if the first field is empty, indicating an empty line
        if not row_data[0].strip():
            continue

        # Extração dos dados comuns a todos os alunos da ata
        # Extração do ano letivo
        if not i_ano:
            if 'Ano Letivo' in row_data:
                i_ano_index = row_data.index('Ano Letivo')
                i_ano = row_data[i_ano_index + 1].strip()
                print("Ano letivo extraído:", i_ano)
            else:
                i_ano = ""
        # Extração da turma
        if not i_turma:
            if 'Turma' in row_data:
                turma_index = row_data.index('Turma')
                i_turma = row_data[turma_index + 1].strip()
                print("Turma extraída:", i_turma)
                # Extração da série, para uso na etapa de confecção do histórico escolar
                i_serie = i_turma[:2].strip()
                print("Série extraída:", i_serie)
            else:
                i_turma = ""

        # Pula as linhas até a 12, onde estão os dados do estudante
        if line_index < 11:
            continue
        
        # Store student data only if it's not empty
        if row_data[2].strip():
            # Extrai o nome do estudante
            nome = row_data[2]
            # Extrai as notas do estudante
            notas = row_data[3:17]
            # Cria uma instância do banco de dados e atribui valores aos campos
            registro_estudante = AtaResultados(
                turma=i_turma,
                serie=i_serie,
                ano=i_ano,
                aluno=nome,
                nt_art=notas[0],
                nt_bio=notas[1],
                nt_edf=notas[2],
                nt_fil=notas[3],
                nt_fis=notas[4],
                nt_geo=notas[5],
                nt_his=notas[6],
                nt_lin=notas[7],
                nt_lpt=notas[8],
                nt_mat=notas[9],
                nt_pro=notas[10],
                nt_qui=notas[11],
                nt_soc=notas[12],
                nt_tec=notas[13]
            )
            # Salva os dados do estudante no banco de dados
            registro_estudante.save()

def emitir_historico(request):
  anos = AtaResultados.objects.values_list('ano', flat=True).distinct()
  turmas = AtaResultados.objects.values_list('turma', flat=True).distinct()

  if request.method == 'POST':
    print("Método POST acessado")
    selected_ano = request.POST.get('ano')
    # Check if selected_ano is empty before using it in filters
    if selected_ano:
      turmas = AtaResultados.objects.filter(ano=selected_ano).values('turma').distinct()
      print("Lista de turmas", turmas)
    else:
      turmas = "Selecionar Turma"  # Set turmas to empty list if no ano is selected
    alunos = "Selecionar Aluno"
    if request.POST.get('turma'):  # Check if turma is also selected in the form
      alunos = AtaResultados.objects.filter(turma=request.POST.get('turma')).values('aluno').distinct()

    return render(request, 'emitir_historico.html', {'anos': anos, 'selected_ano': selected_ano, 'turmas': turmas, 'alunos': alunos})

  elif request.method == 'GET':
    print("Método GET acessado")
    selected_ano = request.GET.get('ano')
    print("Ano a ser pesquisado:", selected_ano)
    if selected_ano:
      print("Ano", selected_ano, "selecionado como filtro")
      turmas = AtaResultados.objects.filter(ano=selected_ano).values('turma').distinct()
      print("Turmas filtradas:", turmas)
      # Filter alunos based on turma (and potentially ano)
      alunos = AtaResultados.objects.filter(turma__in=turmas).values('aluno').distinct()
      # Prepare a dictionary containing both turmas and alunos data
      data = {'turmas': list(turmas), 'alunos': list(alunos)}
      # Return JSON response with the data dictionary
      return JsonResponse(data, safe=False)
    else:
      turmas = "Selecionar Turma"  # Set turmas to empty list if no ano is selected
      alunos = "Selecionar Aluno"

    return render(request, 'emitir_historico.html', {'anos': anos, 'selected_ano': selected_ano, 'turmas': turmas, 'alunos': alunos})
