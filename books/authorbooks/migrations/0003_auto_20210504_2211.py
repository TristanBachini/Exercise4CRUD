# Generated by Django 3.1.7 on 2021-05-05 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authorbooks', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='pagenum',
            new_name='number_of_pages',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authorbooks.author'),
        ),
    ]
