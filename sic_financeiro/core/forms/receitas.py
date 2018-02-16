from django import forms

from sic_financeiro.core.globais import utils
from sic_financeiro.core.models import Receita


class ContasForm(forms.ModelForm):
    saldo = forms.CharField(
        label='Valor',
        widget=forms.TextInput(attrs={
            'class': 'form-control moeda-real',
            'required': True,
            'placeholder': 'R$ 0,00'
        }))

    class Meta:
        model = Receita
        fields = ['descricao', 'data_receita', 'valor', 'status_recebida', 'tipo', 'conta', 'tags', 'observacoes',
                  'repeticao', 'receita_fixa', 'numero_repeticoes']
        labels = {
            'descricao': 'Nome da Receita',
            'data_receita': 'Data',
            'status_recebida': 'Recebida?',
            'observacoes': 'Observações',
            'receita_fixa': 'Receita Fixa?'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Nome da Conta'}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }

    def clean_saldo(self):
        return utils.remove_moeda(self.cleaned_data['saldo'])

