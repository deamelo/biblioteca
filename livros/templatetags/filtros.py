from django import template

register = template.Library()

@register.filter
def tempo_duracao(inicio, fim):
    return (inicio - fim).days