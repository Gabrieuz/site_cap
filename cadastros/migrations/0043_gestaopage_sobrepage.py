# Generated by Django 4.0.2 on 2022-03-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0042_alter_pilares_pilar_three_alter_pilares_titulo_one_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GestaoPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome:')),
                ('cargo', models.CharField(max_length=200, verbose_name='Cargo:')),
                ('twitter', models.URLField(default='https://www.twitter.com', verbose_name='Twitter:')),
                ('face', models.URLField(default='https://www.facebook.com', verbose_name='Facebook:')),
                ('insta', models.URLField(default='https://www.instagram.com', verbose_name='Instagran:')),
                ('linkedin', models.URLField(default='https://www.linkedin.com', verbose_name='Linkedin:')),
                ('imagem', models.ImageField(default='fotos/fotos_padrao.png', upload_to='foto', verbose_name='Imagem:')),
            ],
        ),
        migrations.CreateModel(
            name='SobrePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, default='Histórico do Colégio de Aplicação da Ufac', max_length=50, null=True, verbose_name='Título:')),
                ('subtitulo', models.CharField(blank=True, default='Aqui são "retalhos" do nosso Projeto Político-Pedagógico - 2013–2016', max_length=100, null=True, verbose_name='Subtitulo:')),
                ('texto', models.TextField(blank=True, default='No Brasil, os Colégios de Aplicação oferecem diversas modalidades de ensino – da Pré-Escola à Pós-Graduação. A estrutura administrativa é diferente e pode variar de universidade para universidade, enquanto que a pedagógica é bastante parecida, pois todos têm como base as inovações pedagógicas e o atendimento aos estagiários dos cursos de licenciatura das universidades às quais estão vinculados, contribuindo com a formação inicial e continuada de professores das redes básicas – a partir de projetos e parcerias institucionais.', max_length=1000, null=True, verbose_name='Texto:')),
                ('imagem', models.ImageField(default='imagens/imagem_padrao.png', upload_to='imagens', verbose_name='Imagem:')),
            ],
        ),
    ]
