# Generated by Django 3.2.7 on 2021-10-17 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_education'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='title',
        ),
    ]