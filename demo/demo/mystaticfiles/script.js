$(document).ready(function() {
  console.log("Jquery loaded and ready for use!")
  // Update turma and aluno options based on selected ano
  $("#ano").change(function() {
    var selectedAno = $(this).val();
    console.log("Ano selecionado:", selectedAno);
    if (selectedAno) {
      console.log("Recuperação de turma iniciada");
      // Assuming you have a URL to fetch turmas based on ano
      $.ajax({
        url: '/emitir_historico/', 
        type: 'GET',
        data: { ano: selectedAno }, // Send data as query parameters
        success: function(data) {
          console.log("Sucesso na recuperação de turma:", data); // Inspect data structure
          console.log("Lista de Turmas:", data.turmas)
          $("#turma").empty(); // Clear previous turma options
          $("#turma").append('<option value="">Selecionar Turma</option>');
          for (var i = 0; i < data.turmas.length; i++) {
            // **Option structure as requested**
            var option = `<option value="${data.turmas[i].turma}">${data.turmas[i].turma}</option>`;
            console.log("Opção adiconada à lista:", option);
            $("#turma").append(option);
          }
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.error('Error fetching turmas:', errorThrown);
        }
      });
    } else {
      $("#turma").empty(); // Clear turma options if ano is not selected
      $("#aluno").empty(); // Clear aluno options as well
    }
  });

  // Update aluno options based on selected turma (assuming nested URL)
  $("#turma").change(function() {
    var selectedAno = $("#ano").val();
    console.log("Ano selecionado para o aluno:", selectedAno);
    var selectedTurma = $(this).val();
    console.log("Turma selecionada para o aluno:", selectedTurma)
    if (selectedTurma) {
      console.log("Recuperação de aluno iniciada");
      $.ajax({
        url: '/emitir_historico/', // Replace with your actual view URL
        type: 'GET',
        data: { ano: selectedAno, turma: selectedTurma }, // Send data as query parameters
        success: function(data) {
          console.log("Sucesso na recuperação de aluno:", data);
          console.log("Lista de Alunos:", data.alunos)
 
          // Existing code to populate aluno dropdown
          $("#aluno").empty(); // Clear previous aluno options
          $("#aluno").append('<option value="">Selecionar Aluno</option>');
          for (var i = 0; i < data.alunos.length; i++) {
            var option = `<option value="${data.alunos[i].aluno}">${data.alunos[i].aluno}</option>`;
            console.log("Alunos recuperados corretamente")
            //console.log("Opção adiconada à lista:", option);
            $("#aluno").append(option);
          }
  
  // Recuperação das notas armazenadas no banco de dados para o aluno selecionado
  $("#aluno").change(function() {
    var selectedAno = $("#ano").val();
    console.log("Ano selecionado para o aluno:", selectedAno);
    var selectedTurma = $("turma").val();
    console.log("Turma selecionada para o aluno:", selectedTurma)
    var selectedAluno =$(this).val();
    console.log("O aluno selecionado para as notas serem exibidas foi:", selectedAluno)
    if (selectedAluno) {
      console.log("Recuperação de notas iniciada");
      $.ajax({
        url: '/emitir_historico/', // Replace with your actual view URL
        type: 'GET',
        data: { ano: selectedAno, turma: selectedTurma, aluno: selectedAluno }, // Send data as query parameters
        success: function(data) {
          console.log("Sucesso na recuperação das notas do aluno:", data);

          var selectedAluno = $("#aluno").val();
  
          for (var i = 0; i < data.alunos.length; i++) {
            if (data.alunos[i].aluno === selectedAluno) {
              // Found matching student, update grades
              var studentGrades = data.alunos[i];
              for (var subject in studentGrades) {
                if (subject.startsWith("nt_")) { // Check if key starts with "nt_" (grade)
                  var gradeElement = $("#grade_" + subject.substring(3)); // Extract subject name
                  gradeElement.text(studentGrades[subject]);
                }
              }
              break; // Exit loop after finding the matching student
            }
          }
          
          }
        });
      };
    });
  }
});
};
});
});

          
              