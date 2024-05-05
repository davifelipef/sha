// Carrega o script depois que todos os elementos da página são carregados
document.addEventListener('DOMContentLoaded', function() {
    function fecharMensagem() {
        document.getElementById('mensagem-confirmacao').style.display = 'none';
        // Limpar o campo de envio de arquivo
        document.getElementById('filename').value = '';
    }
})