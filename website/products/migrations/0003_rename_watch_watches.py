# Generated by Django 5.1.7 on 2025-04-15 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_watch_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='watch',
            new_name='watches',
        ),
    ]
