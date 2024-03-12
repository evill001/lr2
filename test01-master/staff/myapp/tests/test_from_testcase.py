# from unittest import skip
# from django.test import TestCase
# from myapp.forms import TaskForm
#
#
# class FormTest(TestCase):
#     def test_form_valid(self):
#         form_data = {'name': 'Часы X'}
#         form = TaskForm(data=form_data)
#         self.assertFalse(form.is_valid())
#
#     def test_form_invalid(self):
#         form_data = {'name': ''}
#         form = TaskForm(data=form_data)
#         self.assertFalse(form.is_valid())