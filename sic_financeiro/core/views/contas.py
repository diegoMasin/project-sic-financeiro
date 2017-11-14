from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from sic_financeiro.core.forms.contas import ContasForm
from sic_financeiro.core.globais import carregador_global
from sic_financeiro.core.globais.utils import set_usuario_owner
from sic_financeiro.core.models.contas import Conta


@login_required
def listar(request):
    contas = Conta.objects.all().order_by('nome')
    carregador_global.context['lista_contas'] = contas

    return render(request, '{0}/listar.html'.format(carregador_global.path_contas), carregador_global.context)


@login_required
def salvar(request):
    form = ContasForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            dados = form.cleaned_data
            dados['data_inicio'] = datetime.now()

            data = set_usuario_owner(request, dados)
            salvar_conta = Conta(**data)
            salvar_conta.save()

            messages.success(request, 'Nova conta criada com Sucesso!')

        else:
            messages.warning(request, 'O formulário não esta válido {0}'.format(form.errors))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
