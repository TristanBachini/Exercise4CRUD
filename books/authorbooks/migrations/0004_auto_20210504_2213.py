# Generated by Django 3.1.7 on 2021-05-05 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorbooks', '0003_auto_20210504_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
