from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
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
                processar_e_salvar_dados(uploaded_file)  # Use filename directly
                # Exibir mensagem de confirmação
                messages.success(request, 'Ata importada com sucesso!')
                # Limpar o campo de envio de arquivo
                return redirect('importar_ata')
            except ValidationError as e:
                messages.error(request, e.message)
                return render(request, 'importar_ata.html')
    return render(request, 'importar_ata.html')

def processar_e_salvar_dados(uploaded_file):
    csv_file = uploaded_file
    decoded_file = csv_file.read().decode('utf-8').splitlines()

    # Start with an empty list to store data for each student
    data_stored = []

    for line in decoded_file:  

        # Skip empty lines
        if not line.strip():
            continue
        
        # Split the line by semicolons to extract data
        row_data = line.split(';')

        # Check if the first field is empty, indicating an empty line
        if not row_data[0].strip():
            continue

        # Access specific fields in specific rows
        ano = row_data[1] if decoded_file.index(line) == 4 else None
        turma = row_data[1] if decoded_file.index(line) == 8 else None
        serie = turma[:2] if turma is not None else None
        
        # Print or use the extracted data
        if ano is not None:
            print("Ano:", ano)
        if turma is not None:
            print("Turma:", turma)
        if serie is not None:
            print("Série:", serie)

        # Store student data only if it's not empty
        if row_data[2]:
            # Extract data from the row and assign it to variables
            nome = row_data[2]
            nt_arte = row_data[3]
            nt_bio = row_data[4]
            nt_edf = row_data[5]
            nt_fil = row_data[6]
            nt_fis = row_data[7]
            nt_geo = row_data[8]
            nt_his = row_data[9]
            nt_lin = row_data[10]
            nt_lpt = row_data[11]
            nt_mat = row_data[12]
            nt_pro = row_data[13]
            nt_qui = row_data[14]
            nt_soc = row_data[15]
            nt_tec = row_data[16]

            # Create a dictionary to hold the student data
            student_data = {
                'Nome': nome,
                'Arte': nt_arte,
                'Biologia': nt_bio,
                'Ed. Física': nt_edf,
                'Filosofia': nt_fil,
                'Física': nt_fis,
                'Geografia': nt_geo,
                'História': nt_his,
                'Ling. Inglesa': nt_lin,
                'Ling. Portuguesa': nt_lpt,
                'Matemática': nt_mat,
                'Projeto de Vida': nt_pro,
                'Química': nt_qui,
                'Sociologia': nt_soc,
                'Tecnologia': nt_tec
            }

            # Create an instance of AtaResultados and assign values to its fields
            student_entry = AtaResultados(
                turma=turma,
                serie=serie,
                ano=ano,
                aluno=nome,
                nt_art=nt_arte,
                nt_bio=nt_bio,
                nt_edf=nt_edf,
                nt_fil=nt_fil,
                nt_fis=nt_fis,
                nt_geo=nt_geo,
                nt_his=nt_his,
                nt_lin=nt_lin,
                nt_lpt=nt_lpt,
                nt_mat=nt_mat,
                nt_pro=nt_pro,
                nt_qui=nt_qui,
                nt_soc=nt_soc,
                nt_tec=nt_tec
            )
            # Save the instance to the database
            student_entry.save()
            
            # Append student data to the list
            data_stored.append(student_data)

    return data_stored