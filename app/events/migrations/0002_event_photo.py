# Generated by Django 5.1 on 2025-04-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(default=1, upload_to='event_photos/', verbose_name='фотография'),
            preserve_default=False,
        ),
    ]
