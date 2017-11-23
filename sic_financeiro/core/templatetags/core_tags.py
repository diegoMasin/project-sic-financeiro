# coding: utf-8
from django import template

from sic_financeiro.core.masks import Money

register = template.Library()


@register.filter()
def to_mask_money(value):
    return Money().format(value)


@register.filter()
def format_positivo_negativo(value):
    formato_cor = 'success' if value >= 0 else 'danger'

    return formato_cor


@register.filter()
def format_status_conta(value):
    formato_cor = 'success' if value else 'dark'

    return formato_cor
