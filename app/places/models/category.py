from django.db import models


class Category(models.Model):
    name = models.CharField('название', max_length=100)
    description = models.TextField('описание', blank=True, null=True)
    icon = models.ImageField('иконка', upload_to='category_icons/', blank=True, null=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name
