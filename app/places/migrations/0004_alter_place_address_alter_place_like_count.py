# Generated by Django 5.1 on 2025-04-04 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_rename_created_place_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.TextField(verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='place',
            name='like_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество лайков'),
        ),
    ]
