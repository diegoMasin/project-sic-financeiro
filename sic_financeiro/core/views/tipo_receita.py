import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from sic_financeiro.core.default_texts import TextosPadroes
from sic_financeiro.core.forms.tipo_receita import TipoReceitaForm
from sic_financeiro.core.globais import carregador_global
from sic_financeiro.core.globais.utils import set_usuario_owner
from sic_financeiro.core.models.tipo_receita import TipoReceita


NOME_MODELO = 'Tipo de Receita'


@login_required
def listar(request):
    tipo_receita = TipoReceita.objects.all().order_by('nome')
    carregador_global.context['lista_tipo_receita'] = tipo_receita
    carregador_global.context['form_tipo_receita'] = TipoReceitaForm
    carregador_global.context['url_salvar_tipo_receita'] = reverse('tipo_receita_salvar')
    carregador_global.context['url_editar_tipo_receita'] = reverse('tipo_receita_editar')
    carregador_global.context['url_atualizar_tipo_receita'] = reverse('tipo_receita_atualizar')

    return render(request, '{0}/listar.html'.format(carregador_global.path_tipo_receita), carregador_global.context)


@login_required
def salvar(request):
    form = TipoReceitaForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            dados = form.cleaned_data

            data = set_usuario_owner(request, dados)
            salvar_tipo = TipoReceita(**data)
            salvar_tipo.save()

            messages.success(request, TextosPadroes.salvar_sucesso_o(NOME_MODELO))

        else:
            messages.warning(request, '{0} '.format(form.errors))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def editar(request):
    tipo_receita = TipoReceita.objects.get(pk=int(request.GET['id']))
    json_dict = {
        'id_tipo_receita': tipo_receita.pk,
        'nome': tipo_receita.nome,
        'cor_layout': tipo_receita.cor_layout,
    }

    result = json.dumps(json_dict)
    response = HttpResponse(result, content_type='application/json')
    return response


@login_required
def atualizar(request):
    if request.method == 'POST':
        id_tipo_receita = request.POST['id']
        tipo_receita = TipoReceita.objects.get(pk=int(id_tipo_receita))
        form = TipoReceitaForm(request.POST, instance=tipo_receita)
        if form.has_changed():
            if form.is_valid():
                dados = form.cleaned_data
                dados['id'] = int(id_tipo_receita)

                data = set_usuario_owner(request, dados)
                salvar_tipo_receita = TipoReceita(**data)
                salvar_tipo_receita.save()

                messages.success(request, TextosPadroes.atualizar_sucesso_o(NOME_MODELO))

            else:
                messages.warning(request, form.errors.values())

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def apagar(request, id_tipo_receita):
    try:
        tipo_receita = TipoReceita.objects.filter(pk=id_tipo_receita)
        tipo_receita.delete()

    except Exception:
        messages.error(request, TextosPadroes.error_padrao())

    messages.success(request, TextosPadroes.apagar_sucesso_o(NOME_MODELO))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
