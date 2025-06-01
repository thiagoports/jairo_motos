from django import template

register = template.Library()

@register.filter(name='moeda_brasileira')
def moeda_brasileira(valor):
    try:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except:
        return valor
