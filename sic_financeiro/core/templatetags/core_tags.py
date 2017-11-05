# coding: utf-8
from django import template

from sic_financeiro.core.masks import Money

register = template.Library()


@register.filter()
def to_mask_money(value):
    return Money().format(value)
