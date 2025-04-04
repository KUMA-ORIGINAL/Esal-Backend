from django.db import models


class Place(models.Model):
    name = models.CharField('название', max_length=255)
    description = models.TextField('описание')
    photo = models.ImageField('фотография', upload_to='place_photos/')
    rating = models.FloatField('рейтинг', default=0.0)
    address = models.TextField('адрес')
    social_links = models.JSONField('ссылки на социальные сети', blank=True, null=True)
    view_count = models.PositiveIntegerField('Количество просмотров', default=0)
    like_count = models.PositiveIntegerField('Количество лайков', default=0)

    category = models.ForeignKey('Category', related_name='places', on_delete=models.CASCADE, verbose_name='категория')
    likes = models.ManyToManyField('account.User', related_name="place_likes", blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.name
