from django.db import models
from filer.fields.image import FilerImageField

# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = FilerImageField(related_name='slider_image', on_delete=models.CASCADE, verbose_name='Изображение')
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Порядок в слайдере',
    )
    shown = models.BooleanField(default=True, verbose_name='Видимый')

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.description