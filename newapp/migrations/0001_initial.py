# Generated by Django 4.1.7 on 2023-02-25 15:47

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=200)),
                ('contrasena', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('descripcion', models.CharField(max_length=1000, verbose_name=django.db.models.fields.TextField)),
                ('ultima_conexion', models.DateTimeField(auto_now=True)),
                ('creacion_pefil', models.DateTimeField(auto_now_add=True)),
                ('seguidores', models.IntegerField(default=0)),
                ('seguidos', models.IntegerField(default=0)),
            ],
        ),
    ]