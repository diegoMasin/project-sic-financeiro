from django import forms

from sic_financeiro.core.globais import utils
from sic_financeiro.core.models import Conta


class ContasForm(forms.ModelForm):
    saldo = forms.CharField(
        label='Saldo Atual',
        widget=forms.TextInput(attrs={
            'class': 'form-control moeda-real',
            'required': True,
            'placeholder': 'R$ 0,00'
        }))

    class Meta:
        model = Conta
        fields = ['nome', 'cor_layout', 'tipo', 'saldo']
        labels = {
            'nome': 'Nome',
            'tipo': 'Tipo de Conta',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Nome da Conta'}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }

    def clean_saldo(self):
        return utils.remove_moeda(self.cleaned_data['saldo'])
