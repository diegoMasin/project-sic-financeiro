/** SIGNUP **/
$(document).ready(function(){

    var inputs = $('form').find('input[type="password"]');

    if (inputs !== 'undefined') {
        $(inputs[1]).focusout(function () {
            console.log('Saiu do input!');
            if ($(this).val() !== $(inputs[0]).val())
            {
                console.log('Senha não corresponde! Por favor, redigite a senha.');
            }
        });
    }

});
