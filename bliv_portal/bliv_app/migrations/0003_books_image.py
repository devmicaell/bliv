# Generated by Django 5.1.1 on 2024-09-09 17:56

import bliv_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bliv_app', '0002_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=bliv_app.models.upload_image_book),
        ),
    ]
