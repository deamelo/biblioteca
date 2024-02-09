from django.db import models
from datetime import date

from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_author = models.CharField(max_length=30, blank=True, null=True)
    data_cadastro = models.DateField(default=date.today)
    esprestado = models.BooleanField(default=False)
    nome_solicitante = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    duracao_emprestimo = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome
