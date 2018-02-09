(function ($) {
    var nome = $('#form-tipo-despesa #id_nome');
    var cor_layout = $("#form-tipo-despesa input[name = 'cor_layout']");
    var cor_layout_padrao = $("#form-tipo-despesa input[name = 'cor_layout'][value = 'default']");

    // FUNÇÕES GERAIS
    function resetando_campos_form() {
        nome.val('');
        cor_layout_padrao.prop('checked', true);
    }

    // RESSETAR CAMPOS TODA VEZ QUE ABRIR PARA CRIAR NOVO
    $('#criar-tipo-despesa').click(function() {
        resetando_campos_form();
        $('#form-tipo-despesa').attr('action', URL_SALVAR_TIPO_DESPESA);
    });

    //Capturando Url e trazendo dados do banco.
    $('.btn-editar-tipo-despesa').click(function(event) {
        resetando_campos_form();
        event.preventDefault();
        var id = $(this).data('id');
        $('#form-tipo-despesa').attr('action', URL_ATUALIZAR_TIPO_DESPESA);

        $.ajax({
            url: URL_EDITAR_TIPO_DESPESA,
            type: 'GET',
            dataType: 'json',
            data: {id: id},
            success: function(json) {
                $('#form-tipo-despesa #id_nome').val(json.nome);
                var cor = json.cor_layout;
                $('#form-tipo-despesa').find("input[value=" + cor + "]").prop('checked', true);
                $('#id-tipo-despesa-hidden').val(json.id_tipo_despesa);
            }
        });
    });

})
(jQuery);