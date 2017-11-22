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

    },
        //init
        $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing
    function ($) {
        "use strict";
        $.SweetAlert.init()
    }(window.jQuery);