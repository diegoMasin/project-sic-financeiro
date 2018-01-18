from django.conf.urls import url

from sic_financeiro.core.views import home
from sic_financeiro.core.views import contas
from sic_financeiro.core.views import tags

urlpatterns = [
    url(r'^$', home.pagina_inicial, name='pagina_inicial'),

    url(r'^contas/$', contas.listar, name='contas_listar'),
    url(r'^contas/salvar$', contas.salvar, name='contas_salvar'),
    url(r'^contas/arquivar/(?P<id_conta>(\d+))/$', contas.arquivar, name='contas_arquivar'),


    url(r'^tags/$', tags.listar, name='tags_listar'),
    url(r'^tags/salvar/$', tags.salvar, name='tags_salvar'),
    url(r'^tags/apagar/(?P<id_tag>(\d+))/$', tags.apagar, name='tags_apagar'),
    url(r'^tags/editar/$', tags.editar, name='tags_editar'),
    url(r'^tags/atualizar/$', tags.atualizar, name='tags_atualizar'),
]
