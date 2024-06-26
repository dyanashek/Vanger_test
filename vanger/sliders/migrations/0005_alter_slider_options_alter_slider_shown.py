# Generated by Django 4.2.13 on 2024-05-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sliders', '0004_alter_slider_options_slider_shown_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['my_order'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='slider',
            name='shown',
            field=models.BooleanField(default=True, verbose_name='Видимый'),
        ),
    ]
