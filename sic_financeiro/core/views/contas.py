from django.shortcuts import render
from sic_financeiro.core.views.context_urls import context_urls as carregador_global


def listar(request):
    valor_atual = 3000
    valor_final_mes = 254.50

    carregador_global.context['valor_atual'] = valor_atual
    carregador_global.context['valor_final_mes'] = valor_final_mes

    return render(request, '{0}/listar.html'.format(carregador_global.path_contas), carregador_global.context)
