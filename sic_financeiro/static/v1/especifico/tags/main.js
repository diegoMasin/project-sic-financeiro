(function ($) {

    //Capturando Url e trazendo dados do banco.
    $('.modal-editar-tag').click(function(event) {
        event.preventDefault();
        var id = $(this).data('id');

        $.ajax({
            url: URL_EDITAR_TAG,
            type: 'GET',
            dataType: 'json',
            data: {id: id},
            success: function(json) {
                $('#form-editar-tag #id_nome').val(json.nome);
                $('#id-tag-hidden').val(json.id_tag);
            }
        });
    });

})
(jQuery);