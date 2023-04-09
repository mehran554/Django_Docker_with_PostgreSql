from django import template

register = template.Library()


@register.filters
def convert_digit(value):
    value = str(value)
    persian = '۰۱۲۳۴۵۶۷۸۹'
    english = '0123456789'
    en_to_per_table = value.maketrans(english, persian)
    return value.translate(en_to_per_table)
