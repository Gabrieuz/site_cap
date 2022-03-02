# Generated by Django 4.0.2 on 2022-03-02 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0025_alter_contatopage_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatopage',
            name='mapaCap',
            field=models.TextField(default='<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d15718.196648683606!2d-67.8106109!3d-9.9714163!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x589d3c359dec27ca!2zQ29sw6lnaW8gZGUgQXBsaWNhw6fDo28gZGEgVWZhYw!5e0!3m2!1spt-BR!2sbr!4v1644278509347!5m2!1spt-BR!2sbr" frameborder="0" style="border:0; width: 100%; height: 384px;" allowfullscreen></iframe>', verbose_name='Iframe do Mapa: '),
        ),
        migrations.AlterField(
            model_name='contatopage',
            name='legenda',
            field=models.CharField(blank=True, default='Aqui disponibilizamos várias formas para nos encontrar', max_length=200, null=True, verbose_name='Legenda:'),
        ),
    ]
