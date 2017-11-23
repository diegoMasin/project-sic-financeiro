from django.conf.urls import url

from sic_financeiro.core.views import home
from sic_financeiro.core.views import contas

urlpatterns = [
    url(r'^$', home.pagina_inicial, name='pagina_inicial'),

    url(r'^contas/$', contas.listar, name='contas_listar'),
    url(r'^contas/salvar$', contas.salvar, name='contas_salvar'),
]
