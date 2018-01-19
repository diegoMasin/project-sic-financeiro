(function ($) {
    var nome = $('#form-criar-conta #id_nome');
    var tipo = $('#form-criar-conta #id_tipo');
    var saldo = $('#form-criar-conta #id_saldo');
    var cor_layout = $("#form-criar-conta input[name = 'cor_layout']");
    var cor_layout_padrao = $("#form-criar-conta input[name = 'cor_layout'][value = 'default']");


    // RESET CAMPOS SEMPRE QUE ABRIR MODAL
    $('#menu-criar-conta').click(function () {
        resetando_campos_form();
    });

    // FUNÇÕES GERAIS
    function resetando_campos_form() {
        nome.val('');
        tipo.val('');
        saldo.val('');
        cor_layout_padrao.prop('checked', true);
    }

    //Capturando Url e trazendo dados do banco.
    $('.modal-editar-conta').click(function(event) {
        event.preventDefault();
        var id = $(this).data('id');

        $.ajax({
            url: URL_EDITAR_CONTA,
            type: 'GET',
            dataType: 'json',
            data: {id: id},
            success: function(json) {
                $('#form-editar-conta #id_nome').val(json.nome);
                $('#form-editar-conta #id_tipo').val(json.tipo);
                var saldo_edita = 'R$ ' + json.saldo.replace('.', ',');
                $('#form-editar-conta #id_saldo').val(saldo_edita);
                var cor = json.cor_layout;
                $('#form-editar-conta input:radio[name=cor_layout]:checked').prop('checked', false)
                $('#form-editar-conta').find("input[value=" + cor + "]").prop('checked', true);
                $('#id-conta-hidden').val(json.id_conta);
            }
        });
    });

})
(jQuery);