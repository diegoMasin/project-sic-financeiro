from django.contrib.auth.models import User
from django.db import models

from sic_financeiro.core.models.contas import Conta
from sic_financeiro.core.models.tipo_receita import TipoReceita


class Receita(models.Model):
    ID_REPETICAO_MESES = 1
    ID_REPETICAO_DIAS = 2
    ID_REPETICAO_SEMANAS = 3
    ID_REPETICAO_ANOS = 4

    TIPO_REPETICAO = (
        (ID_REPETICAO_MESES, 'Meses'),
        (ID_REPETICAO_DIAS, 'Dias'),
        (ID_REPETICAO_SEMANAS, 'Semanas'),
        (ID_REPETICAO_ANOS, 'Anos'),
    )

    id = models.AutoField(primary_key=True, db_column='pk_receita')
    descricao = models.CharField(max_length=100, db_column='descricao_receita')
    data_receita = models.DateTimeField(db_column='data_receita')
    valor = models.DecimalField(max_digits=15, decimal_places=2, db_column='valor_receita')
    status_recebida = models.BooleanField(default=False, db_column='status_recebida_receita')
    tipo = models.ForeignKey(TipoReceita,
                             db_column='fk_tipo_receita', on_delete=models.SET_NULL, null=True, blank=True)
    conta = models.ForeignKey(Conta, db_column='fk_conta_receita', on_delete=models.PROTECT)
    tags = models.CharField(max_length=200, db_column='tags_receita', null=True, blank=True)
    observacoes = models.CharField(max_length=100, db_column='observacoes_receita', null=True, blank=True)

    # Atributos da repetição
    repeticao = models.BooleanField(default=False, db_column='repeticao_receita')
    receita_fixa = models.BooleanField(default=False, db_column='fixa_receita')
    tipo_repeticao = models.IntegerField(choices=TIPO_REPETICAO, db_column='tipo_repeticao_receita', blank=True, null=True)
    numero_repeticoes = models.IntegerField(db_column='num_repeticoes_receita', blank=True, null=True)

    # Usuário Owner
    usuario = models.ForeignKey(User, db_column='fk_user_receita', on_delete=models.PROTECT)
    data_modificacao = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='data_modificacao_receita')

    class Meta:
        db_table = 'tb_receita'

    def __str__(self):
        to_string = self.descricao
        return to_string

    def get_simbolo_receita_recebida(self):
        resultado = []
        simbolo = 'circle-o'
        simbolo = 'check-circle' if self.status_recebida else simbolo
        cor = 'danger'
        cor = 'success' if self.status_recebida else cor
        resultado.append(simbolo)
        resultado.append(cor)

        return resultado
