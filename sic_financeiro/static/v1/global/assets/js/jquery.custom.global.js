(function($) {

    // GERADO DE MENSAGENS
    if($('.gerado-mensagem').length) {
        $('.gerado-mensagem').click();
    }

    // GERADOR DA MASCARA MOEDA REAL
    if($('.moeda-real').length) {
        $('.moeda-real').maskMoney({
            prefix:'R$ ',
            allowNegative: true,
            thousands:'.',
            decimal:',',
            affixesStay: false
        });
    }
})
(jQuery);
