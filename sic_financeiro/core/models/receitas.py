from sic_financeiro.core.models.contas import Conta
from django.contrib.auth.models import User
from sic_financeiro.core.models.tipo_receita import TipoReceita
from django.db import models


class Receita(models.Model):
    id = models.AutoField(primary_key=True, db_column='pk_receita')
    descricao = models.CharField(max_length=100, db_column='descricao_receita')
    data_receita = models.DateTimeField(db_column='data_receita')
    valor = models.DecimalField(decimal_places=2, db_column='saldo_conta')
    status_recebida = models.BooleanField(default=False, db_column='status_recebida_receita')
    tipo = models.ForeignKey(TipoReceita,
                             db_column='fk_tipo_receita', on_delete=models.SET_NULL, null=True, blank=True)
    conta = models.ForeignKey(Conta, db_column='fk_conta_receita', on_delete=models.PROTECT)
    tags = models.CharField(db_column='tags_receita', null=True, blank=True)
    observacoes = models.CharField(max_length=100, db_column='observacoes_receita', null=True, blank=True)

    repeticao = models.BooleanField(default=False, db_column='repeticao_receita')
    receita_fixa = models.BooleanField(default=False, db_column='fixa_receita')
    numero_repeticoes = models.IntegerField(db_column='num_repeticoes_receita')

    # Usuário Owner
    usuario = models.ForeignKey(User, db_column='fk_user_tipo_despesa', on_delete=models.PROTECT)
    data_modificacao = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='data_modificacao_tipo_despesa')

    class Meta:
        db_table = 'tb_tipo_despesa'

    def __str__(self):
        to_string = self.nome
        return to_string
