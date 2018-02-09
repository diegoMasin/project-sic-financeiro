from sic_financeiro.core.forms.contas import ContasForm
from sic_financeiro.core.forms.tags import TagsForm

url_login = 'usuario_login'
url_logout = 'usuario_logout'
url_signup = 'usuario_signup'
url_termo = 'usuario_termo'
url_home = 'pagina_inicial'

url_contas_listar = 'contas_listar'
url_contas_salvar = 'contas_salvar'
url_contas_arquivar = 'contas_arquivar'
url_contas_editar = 'contas_editar'
url_contas_atualizar = 'contas_atualizar'

url_tags_listar = 'tags_listar'
url_tags_salvar = 'tags_salvar'
url_tags_apagar = 'tags_apagar'
url_tags_editar = 'tags_editar'
url_tags_atualizar = 'tags_atualizar'

url_tipo_despesa_listar = 'tipo_despesa_listar'
url_tipo_despesa_salvar = 'tipo_despesa_salvar'
url_tipo_despesa_apagar = 'tipo_despesa_apagar'
url_tipo_despesa_editar = 'tipo_despesa_editar'
url_tipo_despesa_atualizar = 'tipo_despesa_atualizar'

url_tipo_receita_listar = 'tipo_receita_listar'
url_tipo_receita_salvar = 'tipo_receita_salvar'
url_tipo_receita_apagar = 'tipo_receita_apagar'
url_tipo_receita_editar = 'tipo_receita_editar'
url_tipo_receita_atualizar = 'tipo_receita_atualizar'

path_login = 'login'
path_home = 'pagina_inicial'
path_contas = 'contas'
path_tags = 'tags'
path_tipo_despesa = 'tipo_despesa'
path_tipo_receita = 'tipo_receita'

context = {
    'url_login': url_login,
    'url_logout': url_logout,
    'url_signup': url_signup,
    'url_termo': url_termo,
    'url_home': url_home,

    'url_contas_listar': url_contas_listar,
    'url_contas_salvar': url_contas_salvar,
    'url_contas_arquivar': url_contas_arquivar,
    'url_contas_editar': url_contas_editar,
    'url_contas_atualizar': url_contas_atualizar,

    'url_tags_listar': url_tags_listar,
    'url_tags_salvar': url_tags_salvar,
    'url_tags_apagar': url_tags_apagar,
    'url_tags_editar': url_tags_editar,
    'url_tags_atualizar': url_tags_atualizar,

    'url_tipo_despesa_listar': url_tipo_despesa_listar,
    'url_tipo_despesa_salvar': url_tipo_despesa_salvar,
    'url_tipo_despesa_apagar': url_tipo_despesa_apagar,
    'url_tipo_despesa_editar': url_tipo_despesa_editar,
    'url_tipo_despesa_atualizar': url_tipo_despesa_atualizar,

    'url_tipo_receita_listar': url_tipo_receita_listar,
    'url_tipo_receita_salvar': url_tipo_receita_salvar,
    'url_tipo_receita_apagar': url_tipo_receita_apagar,
    'url_tipo_receita_editar': url_tipo_receita_editar,
    'url_tipo_receita_atualizar': url_tipo_receita_atualizar,

    'path_login': path_login,
    'path_home': path_home,
    'path_contas': path_contas,
    'path_tags': path_tags,

    'form_contas': ContasForm(),
    'form_tags': TagsForm(),
}
