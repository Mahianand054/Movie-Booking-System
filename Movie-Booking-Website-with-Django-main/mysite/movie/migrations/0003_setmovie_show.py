# Generated by Django 3.1.5 on 2021-01-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_setmovie'),
    ]

    operations = [
        migrations.AddField(
            model_name='setmovie',
            name='show',
            field=models.CharField(default='morning', max_length=50, verbose_name='Show Time'),
        ),
    ]
