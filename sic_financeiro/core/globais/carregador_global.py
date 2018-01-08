from sic_financeiro.core.forms.contas import ContasForm
from sic_financeiro.core.forms.tags import TagsForm

url_login = 'usuario_login'
url_logout = 'usuario_logout'
url_signup = 'usuario_signup'
url_termo = 'usuario_termo'
url_home = 'pagina_inicial'
url_contas_listar = 'contas_listar'
url_contas_salvar = 'contas_salvar'
url_tags_listar = 'tags_listar'
url_tags_salvar = 'tags_salvar'

path_login = 'login'
path_home = 'pagina_inicial'
path_contas = 'contas'
path_tags = 'tags'

context = {
    'url_login': url_login,
    'url_logout': url_logout,
    'url_signup': url_signup,
    'url_termo': url_termo,
    'url_home': url_home,
    'url_contas_listar': url_contas_listar,
    'url_contas_salvar': url_contas_salvar,
    'url_tags_listar': url_tags_listar,
    'url_tags_salvar': url_tags_salvar,

    'path_login': path_login,
    'path_home': path_home,
    'path_contas': path_contas,
    'path_tags': path_tags,

    'form_contas': ContasForm(),
    'form_tags': TagsForm(),
}
