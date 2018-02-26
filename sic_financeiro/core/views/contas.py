import json
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from sic_financeiro.core.forms.contas import ContasForm
from sic_financeiro.core.globais import carregador_global
from sic_financeiro.core.globais.utils import set_usuario_owner
from sic_financeiro.core.models.contas import Conta


@login_required
def listar(request):
    contas = Conta.objects.filter(usuario=request.user).order_by('nome')
    carregador_global.context['lista_contas'] = contas
    carregador_global.context['total_saldo_atual'] = _calcula_saldo_atual(request)
    carregador_global.context['url_salvar_conta'] = reverse('contas_salvar')
    carregador_global.context['url_editar_conta'] = reverse('contas_editar')
    carregador_global.context['url_atualizar_conta'] = reverse('contas_atualizar')

    return render(request, '{0}/listar.html'.format(carregador_global.path_contas), carregador_global.context)


def _calcula_saldo_atual(request):
    usuario = request.user
    return Conta.objects.filter(usuario=usuario, status_ativa=True).aggregate(Sum('saldo'))['saldo__sum']


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


@login_required
def editar(request):
    conta = Conta.objects.get(pk=int(request.GET['id']))
    json_dict = {
        'id_conta': conta.pk,
        'nome': conta.nome,
        'tipo': conta.tipo,
        'saldo': str(conta.saldo),
        'cor_layout': conta.cor_layout,
    }

    result = json.dumps(json_dict)
    response = HttpResponse(result, content_type='application/json')
    return response


@login_required
def atualizar(request):
    if request.method == 'POST':
        id_conta = request.POST['id']
        conta = Conta.objects.get(id=int(id_conta))
        form = ContasForm(request.POST, instance=conta)
        if form.has_changed():
            if form.is_valid():
                dados = form.cleaned_data
                dados['id'] = int(id_conta)
                dados['data_inicio'] = conta.data_inicio

                data = set_usuario_owner(request, dados)
                salvar_conta = Conta(**data)
                salvar_conta.save()

                messages.success(request, 'Conta atualizada com Sucesso!')

            else:
                messages.warning(request, form.errors.values())

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def arquivar(request, id_conta):
    conta = Conta.objects.get(pk=id_conta)
    if conta.status_ativa:
        conta.status_ativa = False

    else:
        conta.status_ativa = True

    conta.save()
    messages.success(request, 'Conta foi arquivada com sucesso.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
