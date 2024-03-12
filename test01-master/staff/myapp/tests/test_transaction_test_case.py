from unittest import skip
from django.test import TransactionTestCase
from myapp.models import Task


@skip('Пропускаю тест транзакции')
class WidgetTransactionTestCase(TransactionTestCase):
    def test_widget_creation(self):
        Task.objects.create(name='Телефон Samsung')
        Task.objects.create(name='Пылесос LG')
        self.assertEqual(Task.objects.count(), 2)
