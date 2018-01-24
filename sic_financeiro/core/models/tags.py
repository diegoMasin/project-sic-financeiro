from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    id = models.AutoField(primary_key=True, db_column='pk_tag')
    nome = models.CharField(max_length=100, db_column='nome_tag')
    # Usuário Owner
    usuario = models.ForeignKey(User, db_column='fk_user_tag', on_delete=models.PROTECT)
    data_modificacao = models.DateTimeField(null=True, blank=True, auto_now=True, db_column='data_modificacao_tag')

    class Meta:
        db_table = 'tb_tag'

    def __str__(self):
        to_string = self.nome
        return to_string
