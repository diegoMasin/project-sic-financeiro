/** SIGNUP **/
function showMessageNotify(text) {
    //$('.gerado-mensagem').attr('onclick', '2');
    $('.gerado-mensagem').attr('onclick', '$.Notification.autoHideNotify(\'warning\', \'top right\', \'Mensagem:\',\''+text+'\')');
    $('.gerado-mensagem').click();
}

function validPasswordsEqual(inputs) {
    if ($(inputs[1]).val() !== $(inputs[0]).val() || (!$.trim($(inputs[1]).val()) && !$.trim($(inputs[0]).val()))) {
        showMessageNotify('A senha não corresponde! Por favor, repita a senha corretamente.');
        $(inputs).parents('.input-group').addClass('has-warning');
        $(inputs).val('');
        $(inputs[0]).focus();
        return false;
    } else {
        if ($(inputs).parents('.input-group').hasClass('has-warning')) {
            $(inputs).parents('.input-group').removeClass('has-warning');
        }
        return true;
    }
}

$(document).ready(function(){

    var inputs = $('form').find('input[type="password"]');

    if (inputs !== 'undefined') {
        $(inputs[1]).focusout(function () {
            validPasswordsEqual(inputs);
        });

        $('form').submit(function(e) {
            if (!validPasswordsEqual(inputs)) {
                e.preventDefault();
                return false;
            }
        });
    }

});
