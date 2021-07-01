# Generated by Django 3.1.7 on 2021-06-24 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categoria')),
            ],
            options={
                'verbose_name_plural': 'Sub categorías',
                'unique_together': {('categoria', 'descripcion')},
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=50)),
                ('exitencias', models.IntegerField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('subCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subcategoria')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
    ]