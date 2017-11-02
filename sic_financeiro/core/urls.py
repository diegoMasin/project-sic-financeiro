from django.conf.urls import url

from sic_financeiro.core.views import home

urlpatterns = [
    url(r'^$', home.pagina_inicial, name='pagina_inicial'),
]
