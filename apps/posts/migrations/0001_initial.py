from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('fecha_publicacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
