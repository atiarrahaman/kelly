# Generated by Django 3.2.8 on 2021-10-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_auto_20211026_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='maps',
            field=models.TextField(),
        ),
    ]
