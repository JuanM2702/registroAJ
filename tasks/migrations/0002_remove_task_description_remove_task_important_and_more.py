# Generated by Django 4.2.6 on 2023-10-09 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='important',
        ),
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.AddField(
            model_name='task',
            name='cedula',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='task',
            name='centro_costos',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='departamento',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='fecha_ingreso',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='ml',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='task',
            name='nombre_pc',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='nombre_user',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='sede',
            field=models.CharField(default='', max_length=50),
        ),
    ]
