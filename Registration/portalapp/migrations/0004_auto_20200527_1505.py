# Generated by Django 3.0.6 on 2020-05-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0003_auto_20200527_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
