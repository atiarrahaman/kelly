# Generated by Django 3.2.7 on 2021-10-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='bg',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
