# Generated by Django 2.2 on 2021-03-24 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210323_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='name',
            field=models.CharField(default='class', max_length=255),
            preserve_default=False,
        ),
    ]