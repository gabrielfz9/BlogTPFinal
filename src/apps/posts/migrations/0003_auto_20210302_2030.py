# Generated by Django 3.0 on 2021-03-02 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210302_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='miniatura',
            field=models.ImageField(upload_to=''),
        ),
    ]
