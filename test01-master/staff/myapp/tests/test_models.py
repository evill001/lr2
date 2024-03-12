import unittest
from unittest import skip
from django.test import TestCase
from myapp.models import Task

class MyModelTest(TestCase):
    def setUp(self):
        self.object = Task.objects.create(name="Часы", price=100, place='21', img=None, square='Москва')

    def test_str_representation(self):
        self.assertEqual(str(self.object), 'Часы')

    def tearDown(self):
        pass
