# Generated by Django 3.2.7 on 2021-09-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_dog_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dog',
            name='sex',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='dog',
            name='temperment',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dog',
            name='training',
            field=models.CharField(max_length=100),
        ),
    ]
