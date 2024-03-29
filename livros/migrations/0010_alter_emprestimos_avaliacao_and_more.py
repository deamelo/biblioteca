# Generated by Django 5.0.2 on 2024-02-16 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0009_alter_emprestimos_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(blank=True, choices=[('P', 'Pessimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Otimo')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 16, 1, 6, 17, 438954)),
        ),
    ]
