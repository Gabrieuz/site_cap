# Generated by Django 4.0.2 on 2022-03-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0026_contatopage_mapacap_alter_contatopage_legenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatopage',
            name='mapaCap',
            field=models.TextField(default='https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d15718.196648683606!2d-67.8106109!3d-9.9714163!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x589d3c359dec27ca!2zQ29sw6lnaW8gZGUgQXBsaWNhw6fDo28gZGEgVWZhYw!5e0!3m2!1spt-BR!2sbr!4v1644278509347!5m2!1spt-BR!2sbr', verbose_name='Link do Mapa: '),
        ),
    ]
