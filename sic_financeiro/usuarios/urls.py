from django.conf.urls import url

from sic_financeiro.usuarios import views as usuario_view

urlpatterns = [
    url(r'^login/$', usuario_view.login, name='usuario_login'),
    url(r'^signup/$', usuario_view.cadastrar, name='usuario_signup')

]
