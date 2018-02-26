from decimal import Decimal
from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from sic_financeiro.core.default_texts import TextosPadroes


def remove_moeda(string):
    if not string:
        return None

    string = str(string)
    string = string.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')

    return Decimal(string)


@login_required
def set_usuario_owner(request, data):
    from django import forms

    try:
        if isinstance(data, forms.ModelForm) or isinstance(data, forms.Form):
            data = data.cleaned_data

        usuario_logado = request.user
        data['usuario'] = usuario_logado

    except ValueError:
        messages.warning(request, TextosPadroes.usuario_nao_logado())

    return data


def mes_atual():
    return date.today().month


def ano_atual():
    return date.today().year
