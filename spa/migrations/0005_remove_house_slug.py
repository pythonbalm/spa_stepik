# Generated by Django 3.1.7 on 2021-07-27 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0004_auto_20210727_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='slug',
        ),
    ]