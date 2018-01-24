from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

    return render(request, '{0}/listar.html'.format(carregador_global.path_tags), carregador_global.context)

#ctrl + alt + o -- org. imports
#alt + enter (mostra o problema)

@login_required
def salvar(request):
    if request.method == 'POST':
        form = TagsForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            data = set_usuario_owner(request, dados)
            salvar_tag = Tag(**data)
            salvar_tag.save()
            messages.success(request, 'Nova tag criada com sucesso!')
        else:
            messages.warning(request, 'O formulario nao esta valido!'.format(form.errors))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def apagar(request, id_tag):
    tag = Tag.objects.filter(pk=id_tag)
    tag.delete()
    messages.success(request, 'Tag removida com sucesso!')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def editar(request, id_tag):
    pass


@login_required
def atualizar(request, id_tag):
    pass
