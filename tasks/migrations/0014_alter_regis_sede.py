# Generated by Django 4.2.6 on 2023-11-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_alter_regis_sede'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regis',
            name='sede',
            field=models.CharField(default='', max_length=50),
        ),
    ]