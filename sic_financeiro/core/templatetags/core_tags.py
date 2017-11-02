# coding: utf-8
from django import template
from django.utils.html import strip_tags

register = template.Library()


# @register.filter('fieldtype')
# def fieldtype(field):
#     return field.field.widget.__class__.__name__
#
#
# @register.simple_tag
# def limitar_texto(value, **kwargs):
#     palavras = kwargs['palavras']
#     letras = kwargs['letras']
#     texto = strip_tags(value)
#     returno = ''
#     reticencias = False
#     lista_palavras = texto.split()
#
#     if palavras > 0 and len(lista_palavras) > palavras:
#         for x in range(0, palavras):
#             returno += lista_palavras[x] + ' '
#     else:
#         returno = texto
#     if len(returno) > letras:
#         returno = ''
#         if len(lista_palavras) > palavras:
#             palavras = palavras - 1
#         else:
#             palavras = len(lista_palavras) - 1
#
#         for x in range(0, (palavras - 1)):
#             returno += lista_palavras[x] + ' '
#     return returno
