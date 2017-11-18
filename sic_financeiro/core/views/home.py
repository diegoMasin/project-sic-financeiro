from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from sic_financeiro.core.views.context_urls import context_urls as carregador_global


@login_required
def pagina_inicial(request):
    return render(request, '{0}/index.html'.format(carregador_global.path_home), carregador_global.context)
