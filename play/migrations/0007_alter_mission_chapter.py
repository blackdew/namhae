# Generated by Django 4.0.2 on 2023-05-31 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0006_mission_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='chapter',
            field=models.CharField(default='blank', max_length=100),
        ),
    ]