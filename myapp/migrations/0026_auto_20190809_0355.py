# Generated by Django 2.2.dev20180812014849 on 2019-08-09 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_auto_20190809_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='download')),
            ],
        ),
        migrations.DeleteModel(
            name='My_model',
        ),
    ]