# Generated by Django 5.1 on 2025-03-16 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_place_created_place_like_count_place_likes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='updated',
            new_name='updated_at',
        ),
    ]
