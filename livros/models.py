from django.db import models
from datetime import date
import datetime

from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_author = models.CharField(max_length=30, blank=True, null=True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome


class Emprestimos(models.Model):
    choices = (
        ('P', 'Pessimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Otimo'),
    )
    nome_solicitante = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    solicitante_anonimo = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now())
    data_devolucao = models.DateTimeField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)

    class Meta:
        verbose_name = 'Emprestimo'

    def __str__(self) -> str:
        return f"{self.nome_solicitante} | {self.livro}"