# Generated by Django 4.0.2 on 2022-02-13 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='titulo',
            field=models.ImageField(upload_to='uploads/', verbose_name='Escolha a imagem'),
        ),
    ]
