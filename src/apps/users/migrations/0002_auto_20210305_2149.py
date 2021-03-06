# Generated by Django 3.0 on 2021-03-06 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios/avatares'),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='face',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='fechaModif',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='hobby',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='insta',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nacionalidad',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ocupacion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='snapchat',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tiktok',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='wapp',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='web',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='youtube',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
