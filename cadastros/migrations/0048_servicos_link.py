# Generated by Django 4.0.2 on 2022-03-27 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0047_gestaoheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicos',
            name='link',
            field=models.URLField(default='', verbose_name='URL:'),
        ),
    ]
