from django import forms
from sic_financeiro.core.models.tipo_receita import TipoReceita


class TipoReceitaForm(forms.ModelForm):

    class Meta:
        model = TipoReceita
        fields = ['nome', 'cor_layout']
        labels = {
            'nome': 'Nome',
            'cor_layout': 'Cor'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True})
        }
