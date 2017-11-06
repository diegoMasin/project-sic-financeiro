from django.shortcuts import render
from sic_financeiro.usuarios.forms import UserModelForm
from sic_financeiro.core.views.context_urls import context_urls as context_global


def cadastrar(request):
    form = UserModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context_global.context['form'] = form

    return render(request, '{0}/signup.html'.format(context_global.path_login), context_global.context)


def login(request):
    return render(request, '{0}/login.html'.format(context_global.path_login), context_global.context)
