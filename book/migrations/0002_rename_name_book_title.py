# Generated by Django 3.2.23 on 2024-01-03 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
