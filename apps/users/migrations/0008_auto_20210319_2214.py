# Generated by Django 3.0 on 2021-03-20 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210319_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='Foto de Perfil'),
        ),
    ]
