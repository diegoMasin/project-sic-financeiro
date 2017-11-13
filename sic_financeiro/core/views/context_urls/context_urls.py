from sic_financeiro.core.forms.contas import ContasForm

url_login = 'usuario_login'
url_logout = 'usuario_logout'
url_signup = 'usuario_signup'
url_termo = 'usuario_termo'
url_home = 'pagina_inicial'
url_contas_listar = 'contas_listar'

path_login = 'login'
path_home = 'pagina_inicial'
path_contas = 'contas'

context = {
    'url_login': url_login,
    'url_logout': url_logout,
    'url_signup': url_signup,
    'url_termo': url_termo,
    'url_home': url_home,
    'url_contas_listar': url_contas_listar,

    'path_login': path_login,
    'path_home': path_home,
    'path_contas': path_contas,

    'form_contas': ContasForm(),
}
