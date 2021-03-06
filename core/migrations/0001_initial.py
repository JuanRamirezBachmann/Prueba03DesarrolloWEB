# Generated by Django 3.2.5 on 2021-07-25 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idMascota', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Mascota')),
                ('tipoAnimal', models.CharField(max_length=50, verbose_name='Tipo de Animal')),
                ('detalles', models.CharField(max_length=200, verbose_name='Detalles del animal')),
            ],
            options={
                'db_table': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Dadosdebaja',
            fields=[
                ('idBaja', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Baja')),
                ('Cliente', models.CharField(max_length=200, verbose_name='Razon Baja')),
            ],
            options={
                'db_table': 'dadosdebaja',
            },
        ),
    ]
