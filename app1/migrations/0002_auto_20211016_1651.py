# Generated by Django 3.2.8 on 2021-10-16 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutMmain',
        ),
        migrations.RenameField(
            model_name='aboutcontent',
            old_name='title',
            new_name='designation',
        ),
        migrations.AlterField(
            model_name='aboutcontent',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]