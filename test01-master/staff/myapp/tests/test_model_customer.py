from django.test import TestCase
from myapp.models import Task


class CustomersModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Task.objects.create(name='Big', price='1000', place='1231', square ='123')

    def test_first_name_label(self):
        customer = Task.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Имя')

    def test_phone_label(self):
        customer = Task.objects.get(id=1)
        field_label = customer._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'Цена')

    def test_place_max_length(self):
        customer = Task.objects.get(id=1)
        max_length = customer._meta.get_field('place').max_length
        self.assertEqual(max_length, 100)

    def test_square_max_length(self):
        customer = Task.objects.get(id=1)
        max_length = customer._meta.get_field('square').max_length
        self.assertEqual(max_length, 100)
