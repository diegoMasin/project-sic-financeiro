import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from sic_financeiro.core.forms.contas import ContasForm
from sic_financeiro.core.forms.tipo_despesa import TipoDespesaForm
from sic_financeiro.core.globais import carregador_global
from sic_financeiro.core.globais.utils import set_usuario_owner
from sic_financeiro.core.models.contas import Conta
from sic_financeiro.core.models.tipo_despesa import TipoDespesa


@login_required
def listar(request):
    tipo_despesa = TipoDespesa.objects.all().order_by('nome')
    carregador_global.context['lista_tipo_despesa'] = tipo_despesa
    carregador_global.context['form_tipo_despesa'] = TipoDespesaForm
    carregador_global.context['url_salvar_tipo_despesa'] = reverse('tipo_despesa_salvar')
    carregador_global.context['url_editar_tipo_despesa'] = reverse('tipo_despesa_editar')
    carregador_global.context['url_atualizar_tipo_despesa'] = reverse('tipo_despesa_atualizar')

    return render(request, '{0}/listar.html'.format(carregador_global.path_tipo_despesa), carregador_global.context)


@login_required
def salvar(request):
    form = TipoDespesaForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            dados = form.cleaned_data

            data = set_usuario_owner(request, dados)
            salvar_tipo = TipoDespesa(**data)
            salvar_tipo.save()

            messages.success(request, 'Novo Tipo de Despesa criado com Sucesso!')

        else:
            messages.warning(request, '{0} '.format(form.errors))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def editar(request):
    tipo_despesa = TipoDespesa.objects.get(pk=int(request.GET['id']))
    json_dict = {
        'id_tipo_despesa': tipo_despesa.pk,
        'nome': tipo_despesa.nome,
        'cor_layout': tipo_despesa.cor_layout,
    }

    result = json.dumps(json_dict)
    response = HttpResponse(result, content_type='application/json')
    return response


@login_required
def atualizar(request):
    if request.method == 'POST':
        id_conta = request.POST['id']
        conta = Conta.objects.get(id=int(id_conta))
        form = ContasForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            dados['id'] = int(id_conta)
            dados['data_inicio'] = conta.data_inicio

            data = set_usuario_owner(request, dados)
            salvar_tag = Conta(**data)
            salvar_tag.save()

            messages.success(request, 'Conta atualizada com Sucesso!')

        else:
            messages.warning(request, form.errors.values())

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def apagar(request, id_tipo_despesa):
    try:
        tipo_despesa = TipoDespesa.objects.filter(pk=id_tipo_despesa)
        tipo_despesa.delete()

    except Exception:
        messages.error(request, carregador_global.mensagem_error)

    messages.success(request, 'Tipo de Despesa removida com sucesso.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
