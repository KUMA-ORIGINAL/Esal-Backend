from django.db import models


class PlaceImage(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images', verbose_name='место')
    image = models.ImageField('изображение', upload_to='place_images/')

    class Meta:
        verbose_name = 'изображение места'
        verbose_name_plural = 'изображения места'

    def __str__(self):
        return f"Изображение для {self.place.name}"
