from django import template
from datetime import datetime

register = template.Library()

@register.filter
def tempo_duracao(inicio, fim):
    if all((isinstance(inicio, datetime),isinstance(fim, datetime))):
        dias = (inicio - fim).days
        texto = 'dias'
        if dias == 1:
            texto = 'dia'
        return f'{dias} {texto}'
    return 'Emprestado'