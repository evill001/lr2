from django.db import models


class Task(models.Model):
    name = models.CharField('Название', max_length=100)
    price = models.IntegerField('Цена')
    place = models.IntegerField('Количество')
    img = models.ImageField(upload_to="img", default=None, blank=True, null=True, verbose_name="Фото")
    square = models.CharField('Адрес заказа', max_length=100)

    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'
