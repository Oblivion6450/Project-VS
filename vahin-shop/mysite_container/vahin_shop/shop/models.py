from django.db import models

class shop(models.Model):
    img = models.ImageField(upload_to = 'img', verbose_name='Фото')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    status = models.CharField(max_length=10, verbose_name='Статус')
    amount = models.IntegerField(default=1, verbose_name='Выбранное количество')
    price = models.IntegerField(default=0, verbose_name='Цена')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name
        # return '{} {} {} {} {} {} {}'.format(self.amount, self.published, self.img, self.name, self.price, self.status)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']