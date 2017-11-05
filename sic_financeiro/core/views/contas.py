from django.shortcuts import render
from sic_financeiro.core.views.context_urls import context_urls as carregador_global


def listar(request):
    return render(request, '{0}/listar.html'.format(carregador_global.path_contas), carregador_global.context)
