# Generated by Django 5.0.7 on 2024-08-04 23:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_proyectos'),
    ]

    operations = [
        migrations.CreateModel(
            name='tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miapp.proyectos')),
            ],
        ),
    ]
