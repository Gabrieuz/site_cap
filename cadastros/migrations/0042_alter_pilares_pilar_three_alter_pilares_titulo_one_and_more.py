# Generated by Django 4.0.2 on 2022-03-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0041_rename_tituloone_fotospage_titulo_one_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilares',
            name='pilar_three',
            field=models.TextField(blank=True, null=True, verbose_name='Pilar III:'),
        ),
        migrations.AlterField(
            model_name='pilares',
            name='titulo_one',
            field=models.CharField(blank=True, default='MISSÃO', max_length=100, null=True, verbose_name='Título I:'),
        ),
        migrations.AlterField(
            model_name='pilares',
            name='titulo_three',
            field=models.CharField(blank=True, default='VALORES', max_length=100, null=True, verbose_name='Título III:'),
        ),
        migrations.AlterField(
            model_name='pilares',
            name='titulo_two',
            field=models.CharField(blank=True, default='VISÃO', max_length=100, null=True, verbose_name='Título II:'),
        ),
    ]