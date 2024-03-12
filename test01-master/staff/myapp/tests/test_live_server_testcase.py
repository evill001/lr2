from unittest import skip
from django.test import LiveServerTestCase
from selenium import webdriver
from myapp.models import Task
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@skip("test skip")
class NameFunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_product_list_functional(self):
        # Create test data
        Task.objects.create(name="Часы X", price=100, place='212', img=None, square='Москва')
        Task.objects.create(name="Часы VX", price=100, place='21', img=None, square='Москва')

        # Simulate user interactions using Selenium
        self.selenium.get(self.live_server_url + '/')
        self.assertIn('Главная страница сайта', self.selenium.title)
        names = self.selenium.find_elements(By.TAG_NAME, 'td')
        self.assertEqual(len(names), 12)
        self.assertEqual(names[0].text, 'Часы VX')
        self.assertEqual(names[1].text, '21')   # ???
