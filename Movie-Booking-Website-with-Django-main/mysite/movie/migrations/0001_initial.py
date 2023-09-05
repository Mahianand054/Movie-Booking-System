# Generated by Django 3.1.5 on 2021-01-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='MovieMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=50, verbose_name='Movie Name')),
                ('m_desc', models.CharField(max_length=50, verbose_name='Movie Description')),
                ('m_image', models.ImageField(upload_to='pics/', verbose_name='Movie Image')),
            ],
        ),
    ]