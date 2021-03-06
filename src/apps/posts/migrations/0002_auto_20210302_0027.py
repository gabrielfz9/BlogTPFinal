# Generated by Django 3.0 on 2021-03-02 03:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de publicación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='ultima_actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Última actualización'),
        ),
    ]
