# Generated by Django 2.2.24 on 2021-06-09 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleus', '0002_auto_20210609_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='nucleusdata',
            name='new_txt',
            field=models.TextField(blank=True, default='abc', null=True),
        ),
    ]