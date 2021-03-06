# Generated by Django 4.0.2 on 2022-03-27 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0046_alter_gestaopage_imagem_alter_gestaopage_insta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GestaoHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_one', models.CharField(default='Nossa', max_length=100, verbose_name='Título I:')),
                ('titulo_two', models.CharField(default='Gestão', max_length=100, verbose_name='Título II:')),
                ('legenda', models.CharField(blank=True, default='É com alegria que iniciamos o ano letivo de 2022 e o segundo ano da nossa gestão que tem como lema "Com União Podemos Mais".', max_length=300, null=True, verbose_name='Legenda:')),
            ],
        ),
    ]
