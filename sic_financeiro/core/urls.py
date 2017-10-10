from django.conf.urls import url

from sic_financeiro.core.views import index

urlpatterns = [
    url(r'^$', index.home, name='index'),
]
