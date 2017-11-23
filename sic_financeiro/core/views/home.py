from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render

from sic_financeiro.core.globais import carregador_global


@login_required
def pagina_inicial(request):
    context = carregador_global.context
    context['url_contas_salvar_js'] = reverse('contas_salvar')

    return render(request, '{0}/index.html'.format(carregador_global.path_home), context)
