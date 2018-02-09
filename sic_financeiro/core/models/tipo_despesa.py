from django.contrib.auth.models import User
from django.db import models


class TipoDespesa(models.Model):
    AZUL = 'primary'
    VERDE = 'success'
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

    id = models.AutoField(primary_key=True, db_column='pk_tipo_despesa')
    nome = models.CharField(max_length=100, db_column='nome_tipo_despesa', unique=True)
    cor_layout = models.CharField(max_length=10, db_column='cor_layout_tipo_despesa')

    # Usuário Owner
    usuario = models.ForeignKey(User, db_column='fk_user_tipo_despesa', on_delete=models.PROTECT)
    data_modificacao = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='data_modificacao_tipo_despesa')

    class Meta:
        db_table = 'tb_tipo_despesa'

    def __str__(self):
        to_string = self.nome
        return to_string
