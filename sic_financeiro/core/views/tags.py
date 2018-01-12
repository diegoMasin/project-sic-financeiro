from django.core.urlresolvers import reverse
import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from sic_financeiro.core.forms.tags import TagsForm
from sic_financeiro.core.globais import carregador_global
from sic_financeiro.core.globais.utils import set_usuario_owner
from sic_financeiro.core.models.tags import Tag


@login_required
def listar(request):
    tags = Tag.objects.all().order_by('nome')
    carregador_global.context['lista_tags'] = tags
    carregador_global.context['url_editar'] = reverse('tags_editar')

    return render(request, '{0}/listar.html'.format(carregador_global.path_tags), carregador_global.context)


@login_required
def salvar(request):
    if request.method == 'POST':
        form = TagsForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data

            data = set_usuario_owner(request, dados)
            salvar_tag = Tag(**data)
            salvar_tag.save()

            messages.success(request, 'Nova tag criada com Sucesso!')

        else:
            messages.warning(request, 'O formulário não esta válido {0}'.format(form.errors))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def apagar(request, id_tag):
    tag = Tag.objects.filter(pk=id_tag)
    tag.delete()

    messages.success(request, 'Tag removida com sucesso.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def editar(request):
    tag = Tag.objects.get(pk=int(request.GET['id']))
    json_dict = {
        'id_tag': tag.pk,
        'nome': tag.nome
    }

    result = json.dumps(json_dict)
    response = HttpResponse(result, content_type='application/json')
    return response


@login_required
def atualizar(request):
    if request.method == 'POST':
        tag = Tag.objects.get(id=request.POST['id'])
        form = TagsForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            dados['id'] = int(request.POST['id'])

            data = set_usuario_owner(request, dados)
            salvar_tag = Tag(**data)
            salvar_tag.save()

            messages.success(request, 'Tag atualizada com Sucesso!')

        else:
            messages.warning(request, 'O formulário não esta válido {0}'.format(form.errors))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
