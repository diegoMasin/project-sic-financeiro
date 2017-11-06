# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
                'required': True,
                'maxlength': 15
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sobrenome',
                'required': True,
                'maxlength': 15
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': True,
                'maxlength': 100
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'required': True,
                'maxlength': 50
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
                'required': True,
                'maxlength': 50
            }),

        }

        erros_messages = {
            'first_name': {
                'required': 'Este campo é obrigatório.'
            },
            'last_name': {
                'required': 'Este campo é obrigatório.'
            },
            'email': {
                'required': 'Este campo é obrigatório.'
            },
            'username': {
                'required': 'Este campo é obrigatório.'
            },
            'password': {
                'required': 'Este campo é obrigatório.'
            }
        }
