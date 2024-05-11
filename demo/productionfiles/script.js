// Carrega o script depois que todos os elementos da página são carregados
document.addEventListener('DOMContentLoaded', function() {
    function fecharMensagem() {
        document.getElementById('mensagem-confirmacao').style.display = 'none';
        // Limpar o campo de envio de arquivo
        document.getElementById('filename').value = '';
    }

    $(document).ready(function() {
        // Populate 'Turma' dropdown based on selected 'Ano'
        $("#ano").change(function() {
          var selectedAno = $(this).val();
      
          if (selectedAno) {
            $.ajax({
              url: "{% url 'obter_turmas' %}",
              data: { 'ano': selectedAno },
              success: function(response) {
                $("#turma").empty(); // Clear existing options
                $("#turma").append("<option value=''>Selecionar Turma</option>");
      
                for (var i = 0; i < response.length; i++) {
                  var turma = response[i];
                  $("#turma").append("<option value='" + turma.id + "'>" + turma.turma + "</option>");
                }
              }
            });
          } else {
            $("#turma").empty(); // Clear options when 'Ano' is not selected
            $("#aluno").empty(); // Clear 'Aluno' list as well (optional)
          }
        });
      
        // Populate 'Aluno' dropdown based on selected 'Turma'
        $("#turma").change(function() {
          var selectedTurma = $(this).val();
      
          if (selectedTurma) {
            $.ajax({
              url: "{% url 'obter_alunos' %}",
              data: { 'turma': selectedTurma },
              success: function(response) {
                $("#aluno").empty(); // Clear existing options
                $("#aluno").append("<option value=''>Selecionar Aluno</option>");
      
                for (var i = 0; i < response.length; i++) {
                  var aluno = response[i];
                  $("#aluno").append("<option value='" + aluno.id + "'>" + aluno.aluno + "</option>");
                }
              }
            });
          } else {
            $("#aluno").empty(); // Clear options when 'Turma' is not selected
            // Reset student info and grades (optional)
            $("#resultados p").text("-"); // Set empty content for serie and nome
            $("table tbody").empty(); // Clear existing grades
          }
        });
      });
})