# Generated by Django 4.0.2 on 2022-03-06 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0034_alter_contatopage_legenda_alter_fotospage_legenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='legenda',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Legenda (Opcional):'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título:'),
        ),
    ]
