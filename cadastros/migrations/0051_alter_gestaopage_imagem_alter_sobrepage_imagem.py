# Generated by Django 4.0.2 on 2022-03-27 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0050_sobrepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestaopage',
            name='imagem',
            field=models.ImageField(blank=True, default='gestores/gestor_default.png', null=True, upload_to='gestores', verbose_name='Foto:'),
        ),
        migrations.AlterField(
            model_name='sobrepage',
            name='imagem',
            field=models.ImageField(default='pages/sobre_default.jpg', upload_to='pages', verbose_name='Imagem:'),
        ),
    ]