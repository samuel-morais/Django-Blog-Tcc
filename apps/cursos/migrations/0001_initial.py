# Generated by Django 4.0.4 on 2022-04-26 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=200)),
                ('ementa_do_curso', models.TextField()),
                ('informacoes', models.TextField()),
                ('carga_horaria', models.IntegerField()),
                ('categoria', models.CharField(max_length=100)),
                ('data_curso', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]