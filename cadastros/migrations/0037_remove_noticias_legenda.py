# Generated by Django 4.0.2 on 2022-03-06 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0036_alter_noticias_legenda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='legenda',
        ),
    ]
