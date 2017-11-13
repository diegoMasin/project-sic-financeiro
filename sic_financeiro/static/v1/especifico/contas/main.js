(function ($) {
    var nome = $('#id_nome');
    var tipo = $('#id_tipo');
    var saldo = $('#id_saldo');
    var cor_layout = $("input[name = 'cor_layout']");
    var cor_layout_padrao = $("input[name = 'cor_layout'][value = 'CINZA']");


    // RESET CAMPOS SEMPRE QUE ABRIR MODAL
    $('#menu-criar-conta').click(function () {
        resetando_campos_form();
    });

    // AJAX SALVAR CONTA
    $('#salvar-conta').click(function() {
        saldo = saldo.val().replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.');
        saldo = parseFloat(saldo);
        var data = {
            'nome': nome.val(),
            'tipo': tipo.val(),
            'saldo': saldo,
            'cor_layout': cor_layout.val()
        };

        $.ajax({
            type: 'GET',
            url: URL_CONTAS_SALVAR,
            data: data,
            dataType: 'json',
            success: function(json) {
                Console.log(json.mensagem);
            }
        });
    });

    // FUNÇÕES GERAIS
    function resetando_campos_form() {
        nome.val('');
        tipo.val('');
        saldo.val('');
        cor_layout_padrao.prop('checked', true);
    }

})
(jQuery);