# Generated by Django 5.0.2 on 2024-02-10 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0006_alter_emprestimos_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimos',
            name='duracao_emprestimo',
        ),
    ]
