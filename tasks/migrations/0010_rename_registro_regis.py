# Generated by Django 4.2.6 on 2023-10-17 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_registro_remove_task_cedula_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registro',
            new_name='regis',
        ),
    ]
