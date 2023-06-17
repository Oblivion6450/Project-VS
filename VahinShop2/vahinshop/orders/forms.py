from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city']
        labels = {
            'first_name': 'Имя', 'last_name': 'Фамилия', 'address': 'Адрес ПВЗ', 'city': 'Город',
        }