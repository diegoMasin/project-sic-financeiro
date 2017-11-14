from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sic_financeiro.core.models.contas import Conta

from sic_financeiro.core.forms.contas import ContasForm
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
    form = ContasForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        dados = form.cleaned_data
        dados['data_inicio'] = datetime.now()

        Conta.save(**dados)
        # pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # json_dict = {
    #     'mensagem': "Sucesso"
    # }
    # result = json.dumps(json_dict)
    # response = HttpResponse(result, content_type='application/json')
    #
    # return response
