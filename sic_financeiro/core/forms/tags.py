from django import forms
from sic_financeiro.core.models.tags import Tag


class TagsForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['nome']
        labels = {
            'nome': 'Nome'
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'tag'})
        }
