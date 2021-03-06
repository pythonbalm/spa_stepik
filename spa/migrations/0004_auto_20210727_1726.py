# Generated by Django 3.1.7 on 2021-07-27 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0003_house_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='style',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spa.style'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='house',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
