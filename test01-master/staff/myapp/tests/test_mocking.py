from unittest import skip
from django.test import TestCase, RequestFactory
from unittest.mock import Mock, patch
from myapp.models import Task
from myapp.views import index


class TaskListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_name_list_view(self):
        # Create some sample Products objects
        Task.objects.create(name="Часы X", price=100, place='212', img=None, square='Москва')
        Task.objects.create(name="Часы X", price=100, place='212', img=None, square='Москва')

        # Create a mock request object
        request = self.factory.get('/index/')

        # Создайте макетный набор запросов для объектов Products
        mock_queryset = Mock(spec=Task.objects.all())
        mock_queryset.return_value = [
            Mock(name="Часы X", price=100, place='212', img=None, square='Москва'),
            Mock(nname="Часы X", price=100, place='212', img=None, square='Москва')
        ]

        # Исправьте метод Products.objects.all(), чтобы вернуть макетный набор запросов
        with patch('myapp.views.Task.objects.all', mock_queryset):
            # Call the products view
            response = index(request)

        # Assert that the response has the expected status code
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains the expected data
        self.assertContains(response, 'Часы X')
        self.assertContains(response, 'Часы X')
