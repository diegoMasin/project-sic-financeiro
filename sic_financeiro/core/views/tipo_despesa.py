import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from sic_financeiro.core.default_texts import TextosPadroes
from sic_financeiro.core.forms.tipo_despesa import TipoDespesaForm
from sic_financeiro.core.globais import carregador_global
from sic_financeiro.core.globais.utils import set_usuario_owner
from sic_financeiro.core.models.tipo_despesa import TipoDespesa


NOME_MODELO = 'Tipo de Despesa'


@login_required
def listar(request):
    tipo_despesa = TipoDespesa.objects.filter(usuario=request.user).order_by('nome')
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

            messages.success(request, TextosPadroes.salvar_sucesso_o(NOME_MODELO))

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
        id_tipo_despesa = request.POST['id']
        tipo_despesa = TipoDespesa.objects.get(pk=int(id_tipo_despesa))
        form = TipoDespesaForm(request.POST, instance=tipo_despesa)
        if form.has_changed():
            if form.is_valid():
                dados = form.cleaned_data
                dados['id'] = int(id_tipo_despesa)

                data = set_usuario_owner(request, dados)
                salvar_tipo_despesa = TipoDespesa(**data)
                salvar_tipo_despesa.save()

                messages.success(request, TextosPadroes.atualizar_sucesso_o(NOME_MODELO))

            else:
                messages.warning(request, form.errors.values())

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def apagar(request, id_tipo_despesa):
    try:
        tipo_despesa = TipoDespesa.objects.filter(pk=id_tipo_despesa)
        tipo_despesa.delete()

    except Exception:
        messages.error(request, TextosPadroes.error_padrao())

    messages.success(request, TextosPadroes.apagar_sucesso_o(NOME_MODELO))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
