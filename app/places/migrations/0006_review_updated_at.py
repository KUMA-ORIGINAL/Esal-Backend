# Generated by Django 5.1 on 2025-04-10 11:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_remove_place_social_links_place_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата обновления'),
            preserve_default=False,
        ),
    ]
