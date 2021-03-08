<<<<<<< HEAD
# Generated by Django 3.0 on 2021-03-08 20:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
=======
# Generated by Django 3.0 on 2021-03-07 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
>>>>>>> 7fb6e91886da83c4acfe3130d47ff2f1510f5509


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Categoría')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoría activa/Categoría no activa')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título del post')),
                ('contenido', models.TextField(max_length=5255, verbose_name='Contenido del post')),
                ('miniatura', models.ImageField(upload_to='')),
<<<<<<< HEAD
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('fecha_publicacion', models.DateTimeField(default=datetime.datetime(2021, 3, 8, 20, 8, 53, 195126, tzinfo=utc), verbose_name='Fecha de publicación')),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
=======
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('fecha_publicacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
>>>>>>> 7fb6e91886da83c4acfe3130d47ff2f1510f5509
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
