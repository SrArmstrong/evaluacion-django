# Generated by Django 5.1.5 on 2025-02-12 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Pelicula',
        ),
    ]
