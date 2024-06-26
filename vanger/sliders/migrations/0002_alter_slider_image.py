# Generated by Django 4.1.4 on 2024-05-21 05:10

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('sliders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_image', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
