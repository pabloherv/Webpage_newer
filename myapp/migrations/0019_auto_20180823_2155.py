# Generated by Django 2.2.dev20180812014849 on 2018-08-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20180823_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='adicciones',
            field=models.CharField(default=' STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='datos',
            name='ausentismo',
            field=models.CharField(default=' STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='datos',
            name='bajas_calificaciones',
            field=models.CharField(default=' STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='datos',
            name='falta_recursos',
            field=models.CharField(default=' STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='datos',
            name='problemas',
            field=models.CharField(default=' STRING', max_length=30),
        ),
        migrations.AlterField(
            model_name='datos',
            name='violencia',
            field=models.CharField(default=' STRING', max_length=30),
        ),
    ]