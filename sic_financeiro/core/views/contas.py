import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from sic_financeiro.core.views.context_urls import context_urls as carregador_global


@login_required
def listar(request):
    valor_atual = 3000
    valor_final_mes = 254.50

    carregador_global.context['valor_atual'] = valor_atual
    carregador_global.context['valor_final_mes'] = valor_final_mes

    return render(request, '{0}/listar.html'.format(carregador_global.path_contas), carregador_global.context)


@login_required
def salvar(request):
    form = carregador_global.ContasForm(request.GET)
    # if form.is_valid():
    #

    json_dict = {
        'mensagem': "Sucesso"
    }
    result = json.dumps(json_dict)
    response = HttpResponse(result, content_type='application/json')

    return response
