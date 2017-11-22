from django.contrib.auth.models import User
from django.db import models

from sic_financeiro.core.default_texts import TextosPadroes


class Conta(models.Model):
    CONTA_CORRENTE = 1
    POUPANCA = 2
    DINHEIRO = 3
    INVESTIMENTO = 4
    OUTROS = 5
    TIPO_CONTA = (
        ('', TextosPadroes.empty()),
        (CONTA_CORRENTE, 'Conta Corrente'),
        (POUPANCA, 'Conta Poupança'),
        (DINHEIRO, 'Dinheiro na Carteira'),
        (INVESTIMENTO, 'Investimento'),
        (OUTROS, 'Outros Tipos')
    )

    AZUL = 'primary'
    VERDE = 'sucess'
    LARANJA = 'warning'
    VERMELHO = 'danger'
    ROSA = 'pink'
    CINZA = 'default'
    ROXO = 'purple'
    AZUL_CLARO = 'info'
    COR_CONTA = (
        (AZUL, 'Azul'),
        (VERDE, 'Verde'),
        (LARANJA, 'Laranja'),
        (VERMELHO, 'Vermelho'),
        (ROSA, 'Rosa'),
        (CINZA, 'Cinza'),
        (ROXO, 'Roxo'),
        (AZUL_CLARO, 'info')
    )

    id = models.AutoField(primary_key=True, db_column='pk_conta')
    nome = models.CharField(max_length=100, db_column='nome_conta')
    cor_layout = models.CharField(max_length=10, choices=COR_CONTA, db_column='cor_layout_conta')
    tipo = models.IntegerField(choices=TIPO_CONTA, db_column='tipo_conta')
    saldo = models.DecimalField(max_digits=15, decimal_places=2, db_column='saldo_conta')
    status_ativa = models.BooleanField(default=True, db_column='status_ativa_conta')
    # Data determinada a partir do Valor de Saldo Criado ou Alterado
    data_inicio = models.DateField(db_column='data_inicio_conta')

    # Usuário Owner
    usuario = models.ForeignKey(User, db_column='fk_user_conta', on_delete=models.PROTECT)
    data_modificacao = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='data_modificacao_conta')

    class Meta:
        db_table = 'tb_conta'

    def __str__(self):
        to_string = self.nome
        return to_string

    def get_nome_tipo_conta(self):
        return self.TIPO_CONTA[self.tipo][1]

    def get_simbolo_tipo_conta(self):
        simbolo = 'eur'
        simbolo = 'bank' if self.tipo == self.CONTA_CORRENTE else simbolo
        simbolo = 'dollar' if self.tipo == self.POUPANCA else simbolo
        simbolo = 'money' if self.tipo == self.DINHEIRO else simbolo
        simbolo = 'bar-chart-o' if self.tipo == self.INVESTIMENTO else simbolo

        return simbolo

    def get_status_nome(self):
        if self.status_ativa:
            return 'Ativa'

        return 'Arquivada'

    # def get_saldo_final_mês(self):
    #     pass
