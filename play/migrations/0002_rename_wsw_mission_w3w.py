# Generated by Django 4.2 on 2023-05-27 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='wsw',
            new_name='w3w',
        ),
    ]