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
              var option = `<option value="${data.alunos[i].id}">${data.alunos[i].aluno}</option>`;
              console.log("Alunos recuperados corretamente")
              //console.log("Opção adiconada à lista:", option);
              $("#aluno").append(option);
            }

            var studentData = null;
        
            // **New code block for disciplines and grades**
            if (data.length > 0) {
              // Access student data (assuming the first element)
              var studentData = data[0];
              var tableBody = $("#resultados tbody"); // Get the tbody element
            
              // Check if studentData has any fields other than 'aluno' and 'turma' (indicating grades)
              if (Object.keys(studentData).length > 2) {
                console.log("Busca de disciplinas e notas iniciada");
                // Loop through discipline fields and display disciplines and grades
                for (var field in studentData) {
                  if (field !== 'aluno' && field !== 'turma') {
                    var discipline = studentData[field].split("_")[1]; // Extract discipline name
                    var grade = studentData[field];
            
                    // Create and append table row
                    var tableRow = `<tr>
                                      <td>${discipline}</td>
                                      <td>${grade}</td>
                                    </tr>`;
                    tableBody.append(tableRow);
                  }
                }
              } else {
                console.log("A busca por disciplinas e notas não foi iniciada");
                $("#resultados").html('<p>Nenhum resultado encontrado.</p>');
              }
            } else {
              console.log("Um erro ocorreu e a função não foi executada como o planejado");
            }
}})}})})