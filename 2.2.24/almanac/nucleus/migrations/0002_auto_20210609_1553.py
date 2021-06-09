# Generated by Django 2.2.24 on 2021-06-09 15:53

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nucleusdata',
            name='default_json',
            field=django_mysql.models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='nucleusdata',
            name='null_default_blank_txt',
            field=models.TextField(blank=True, default='abc', null=True),
        ),
        migrations.AlterField(
            model_name='nucleusdata',
            name='null_n_default_json',
            field=django_mysql.models.JSONField(default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='nucleusdata',
            name='null_n_default_txt',
            field=models.TextField(default='xyz', null=True),
        ),
    ]