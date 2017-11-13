from django import forms
from sic_financeiro.core.models import Conta


class ContasForm(forms.ModelForm):

    class Meta:
        model = Conta
        fields = ['nome', 'cor_layout', 'tipo', 'saldo']
        labels = {
            'nome': 'Nome',
            'cor_layout': 'Cor de Referência',
            'tipo': 'Tipo de Conta',
            'saldo': 'Saldo Atual'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Nome da Conta'}),
            'cor_layout': forms.RadioSelect(attrs={'class: '}),
            'tipo': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'saldo': forms.TextInput(attrs={
                'class': 'form-control moeda-real',
                'required': True,
                'placeholder': 'R$ 0,00'
            })
        }
