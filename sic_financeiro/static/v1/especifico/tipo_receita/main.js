(function ($) {
    var nome = $('#form-tipo-receita #id_nome');
    var cor_layout = $("#form-tipo-receita input[name = 'cor_layout']");
    var cor_layout_padrao = $("#form-tipo-receita input[name = 'cor_layout'][value = 'default']");

    // FUNÇÕES GERAIS
    function resetando_campos_form() {
        nome.val('');
        cor_layout_padrao.prop('checked', true);
    }

    // RESSETAR CAMPOS TODA VEZ QUE ABRIR PARA CRIAR NOVO
    $('#criar-tipo-receita').click(function() {
        resetando_campos_form();
        $('#form-tipo-receita').attr('action', URL_SALVAR_TIPO_RECEITA);
    });

    //Capturando Url e trazendo dados do banco.
    $('.btn-editar-tipo-receita').click(function(event) {
        resetando_campos_form();
        event.preventDefault();
        var id = $(this).data('id');
        $('#form-tipo-receita').attr('action', URL_ATUALIZAR_TIPO_RECEITA);

        $.ajax({
            url: URL_EDITAR_TIPO_RECEITA,
            type: 'GET',
            dataType: 'json',
            data: {id: id},
            success: function(json) {
                $('#form-tipo-receita #id_nome').val(json.nome);
                var cor = json.cor_layout;
                $('#form-tipo-receita').find("input[value=" + cor + "]").prop('checked', true);
                $('#id-tipo-receita-hidden').val(json.id_tipo_receita);
            }
        });
    });

})
(jQuery);