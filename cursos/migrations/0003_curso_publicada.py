# Generated by Django 4.0.4 on 2022-04-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_curso_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]