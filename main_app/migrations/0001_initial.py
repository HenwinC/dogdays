# Generated by Django 3.2.4 on 2021-09-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('temperment', models.TextField(max_length=150)),
                ('training', models.TextField(max_length=150)),
                ('description', models.TextField(max_length=250)),
                ('sex', models.TextField(max_length=1)),
            ],
        ),
    ]