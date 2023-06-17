# Generated by Django 4.1 on 2023-01-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_shop_basket_shop_published_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='shop',
            name='status',
            field=models.CharField(choices=[('V', 'В наличии'), ('N', 'Нет в наличии')], default='V', max_length=20, verbose_name='Статус'),
        ),
    ]
