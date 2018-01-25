from django import forms
from sic_financeiro.core.models.tipo_despesa import TipoDespesa


class TipoDespesaForm(forms.ModelForm):

    class Meta:
        model = TipoDespesa
        fields = ['nome', 'cor_layout']
        labels = {
            'nome': 'Nome'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'tag'})
        }
