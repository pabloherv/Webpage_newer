# Generated by Django 2.2.dev20180812014849 on 2018-08-24 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_remove_datos_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos',
            name='Fecha',
        ),
    ]