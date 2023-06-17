from django.db import models
from django.urls import reverse

class Product(models.Model):
    img = models.ImageField(upload_to = 'img', verbose_name='Фото')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    amount = models.IntegerField(default=1, verbose_name='Выбранное количество')
    price = models.IntegerField(default=0, verbose_name='Цена')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    class status(models.TextChoices):
        VN = 'V', ('В наличии')
        NV = 'N', ('Нет в наличии')

    status = models.CharField(max_length=20, choices=status.choices,default=status.VN, verbose_name='Статус')
    

    def get_absolute_url(self):
        return reverse('view_shop', kwargs={"shop_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

