# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('fecha', models.DateField()),
                ('cantidad', models.PositiveIntegerField()),
                ('id_producto', models.ForeignKey(to='applications.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('appellido', models.CharField(max_length=50)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='transaccion',
            name='id_usuario',
            field=models.ForeignKey(to='applications.Usuario'),
        ),
        migrations.AddField(
            model_name='producto',
            name='id_usuario',
            field=models.ForeignKey(to='applications.Usuario'),
        ),
    ]
