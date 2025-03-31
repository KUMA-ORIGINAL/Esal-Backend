from django.db import models


class Review(models.Model):
    place = models.ForeignKey('Place', related_name='reviews', on_delete=models.CASCADE, verbose_name='место')
    user = models.ForeignKey('account.User', related_name='reviews', on_delete=models.CASCADE, verbose_name='пользователь')
    text = models.TextField('текст')
    rating = models.IntegerField('оценка')
    created_at = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return f'{self.user.username} - {self.rating}/5'