# Generated by Django 5.0.2 on 2024-02-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0007_remove_emprestimos_duracao_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(choices=[('P', 'Pessimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Otimo')], default=2, max_length=1),
            preserve_default=False,
        ),
    ]