from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
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
