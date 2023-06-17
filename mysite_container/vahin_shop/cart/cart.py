from decimal import Decimal
from django.conf import settings


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

def add(self, shop, amount=1, update_amount=False):
    """
    Добавить продукт в корзину или обновить его количество.
    """
    shop_id = str(shop.id)
    if shop_id not in self.cart:
        self.cart[shop_id] = {'amount': 0,
                                 'price': str(shop.price)}
    if update_quantity:
        self.cart[shop_id]['amount'] = amount
    else:
        self.cart[shop_id]['amount'] += amount
    self.save()

def save(self):
    # Обновление сессии cart
    self.session[settings.CART_SESSION_ID] = self.cart
    # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
    self.session.modified = True

def remove(self, shop):
    """
    Удаление товара из корзины.
    """
    shop_id = str(shop.id)
    if shop_id in self.cart:
        del self.cart[shop_id]
        self.save()

def __iter__(self):
    """
    Перебор элементов в корзине и получение продуктов из базы данных.
    """
    shop_ids = self.cart.keys()
    # получение объектов product и добавление их в корзину
    shops = shop.objects.filter(id__in=shop_ids)
    for shop in shops:
        self.cart[str(shop.id)]['shop'] = shop_item

    for shop_item in self.cart.values():
        shop_item['price'] = Decimal(shop_item['price'])
        shop_item['total_price'] = shop_item['price'] * shop_item['amount']
        yield item

def __len__(self):
    """
    Подсчет всех товаров в корзине.
    """
    return sum(shop_item['amount'] for shop_item in self.cart.values())

def get_total_price(self):
    """
    Подсчет стоимости товаров в корзине.
    """
    return sum(Decimal(shop_item['price']) * shop_item['amount'] for shop_item in self.cart.values())

def clear(self):
    # удаление корзины из сессии
    del self.session[settings.CART_SESSION_ID]
    self.session.modified = True