# Generated by Django 4.0.2 on 2022-03-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0038_alter_fotos_legenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='autor',
            field=models.CharField(blank=True, default='Equipe Gestora', max_length=100, null=True, verbose_name='Autor:'),
        ),
    ]