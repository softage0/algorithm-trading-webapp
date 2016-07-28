from django import template

from ..kiwoom import k_module

register = template.Library()


@register.filter
def get_master_code_name(code):
    result = k_module.get_master_code_name(code)
    return result
