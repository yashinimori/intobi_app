# Generated by Django 4.0.8 on 2022-12-25 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_menu_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='rating',
        ),
    ]
