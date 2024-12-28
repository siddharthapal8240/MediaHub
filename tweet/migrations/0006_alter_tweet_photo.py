# Generated by Django 5.1.4 on 2024-12-28 18:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0005_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photo'),
        ),
    ]
