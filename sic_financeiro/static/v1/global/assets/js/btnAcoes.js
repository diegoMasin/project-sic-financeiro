!function ($) {
    "use strict";

    var SweetAlert = function () {
    };

    SweetAlert.prototype.init = function () {

        //Botão de Ação Arquivar
        $('.acao-arquivar').click(function () {
            swal({
                title: "Você deseja Arquivar?",
                text: "Após arquivada, esta conta sairá dos cálculos.",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Sim, Arquivar!",
                cancelButtonText: "Não, Cancele!",
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal("Arquivada!", "Você Arquivou a conta.", "success");
                } else {
                    swal("Cancelada", "Você não arquivou a conta.", "error");
                }
            });
        });

        //Botão de Ação Arquivar
        $('.acao-excluir').click(function(event) {
            event.preventDefault();
            var url = $(this).data('url');
            var titulo_model = $(this).data('model-title');

            swal({
                title: "Você deseja Excluir?",
                text: "Após excluída, esta " + titulo_model + " deixará de existir.",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Sim, Excluir!",
                cancelButtonText: "Não, Cancele!",
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal({
                        title: 'Excluída!',
                        text: 'Você Excluiu a ' + titulo_model + '.',
                        type: 'success'
                    }, function(){
                        window.location = url;
                    });
                } else {
                    swal("Cancelada", "Você não excluiu a " + titulo_model + ".", "error");
                }
            });
        });

    },
        //init
        $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing
    function ($) {
        "use strict";
        $.SweetAlert.init()
    }(window.jQuery);