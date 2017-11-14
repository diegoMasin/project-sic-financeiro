from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from sic_financeiro.core.globais import carregador_global
from sic_financeiro.usuarios.forms import UserModelForm


def signup(request):
    form = UserModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')

            return redirect('/login')

    context_global.context['form'] = form
    return render(request, '{0}/signup.html'.format(carregador_global.path_login), carregador_global.context)


def do_login(request):
    form = UserModelForm(request.POST or None)
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, 'Bem Vindo ao Sic Financeiro!')

            return redirect(carregador_global.url_home)

        else:
            messages.warning(request, 'Usuário ou senha não existente!')

    carregador_global.context['form'] = form
    return render(request, '{0}/login.html'.format(carregador_global.path_login), carregador_global.context)


@login_required
def do_logout(request):
    logout(request)
    messages.success(request, 'Saiu com Sucesso!')

    return redirect(carregador_global.url_login)


def termo(request):
    return render(request, '{0}/termo_de_uso.html'.format(carregador_global.path_login), carregador_global.context)
