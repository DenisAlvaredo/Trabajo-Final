# Generated by Django 3.0 on 2021-03-17 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='estado',
        ),
    ]
