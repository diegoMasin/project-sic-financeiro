from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from sic_financeiro.core.globais import carregador_global
from sic_financeiro.usuarios.forms import UserModelForm


def signup(request):
    form = UserModelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            try:
                email_form = form.cleaned_data.get('email')
                existe_email = User.objects.filter(email=email_form).count()
                if existe_email > 0:
                    raise Exception('Esse email já foi cadastrado. Utilize outro.')

                is_check_termo = request.POST.get('check_termo', False)
                if not is_check_termo:
                    raise Exception('Marque caixa se concorda com os Termos e Condições!')

                form.save()
                messages.success(request, 'Usuário cadastrado com sucesso!')

                return redirect('/login')

            except Exception as e:
                messages.warning(request, e)
        else:
            if form.errors['username']:
                messages.warning(request, form.errors['username'][0])

    carregador_global.context['form'] = form
    return render(request, '{0}/signup.html'.format(carregador_global.path_login), carregador_global.context)


def do_login(request):
    form = UserModelForm(request.POST or None)
    user_remember_cookie = 'userremember'

    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        is_check_remember = request.POST.get('check_remember', False)

        if is_check_remember:
            if request.session.get(user_remember_cookie, False) is False or request.session[user_remember_cookie] != request.POST['username']:
                request.session[user_remember_cookie] = request.POST['username']
        else:
            if request.session.get(user_remember_cookie, False) is not False:
                del request.session[user_remember_cookie]

        if user is None:
            userqueryset = User.objects.all().filter(email=request.POST['username'])
            if userqueryset:
                username = userqueryset[0].username
                user = authenticate(request, username=username, password=request.POST['password'])

        if user is not None:
            login(request, user)
            messages.success(request, 'Bem Vindo ao Sic Financeiro!')
            return redirect(carregador_global.url_home)
        else:
            messages.warning(request, 'Usuário ou senha não existente!')

    form.fields['username'].initial = request.session.get(user_remember_cookie, '')
    carregador_global.context['form'] = form
    carregador_global.context[user_remember_cookie] = request.session.get(user_remember_cookie, False)
    return render(request, '{0}/login.html'.format(carregador_global.path_login), carregador_global.context)


@login_required
def do_logout(request):
    userremember = request.session.get('userremember', False)
    logout(request)

    if userremember is not False:
        request.session['userremember'] = userremember

    messages.success(request, 'Saiu com Sucesso!')
    return redirect(carregador_global.url_login)


def termo(request):
    return render(request, '{0}/termo_de_uso.html'.format(carregador_global.path_login), carregador_global.context)
