from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    photo = models.ImageField('фотография', upload_to='event_photos/')
    description = models.TextField(blank=True, verbose_name="Описание")
    location = models.CharField(max_length=255, verbose_name="Место проведения")
    start_date = models.DateTimeField(verbose_name="Дата начала")
    end_date = models.DateTimeField(verbose_name="Дата окончания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ['-start_date']

    def __str__(self):
        return self.title
