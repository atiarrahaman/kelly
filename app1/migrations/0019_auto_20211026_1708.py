# Generated by Django 3.2.8 on 2021-10-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_map_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='location',
        ),
        migrations.AddField(
            model_name='map',
            name='maps',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
    ]
