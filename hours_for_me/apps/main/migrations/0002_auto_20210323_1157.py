# Generated by Django 2.2 on 2021-03-23 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='completed',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='class',
            name='completed',
            field=models.BooleanField(),
        ),
    ]