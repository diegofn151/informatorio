# Generated by Django 3.2 on 2022-08-22 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0006_alter_comentario_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['creado']},
        ),
    ]
