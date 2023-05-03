from django.test import TestCase

from .models import Task


class CommonTestCase(TestCase):

    def test_successful_adding_tasks(self):
        Task.objects.create(title='test')
        task = Task.objects.filter().first()
        self.assertEqual(task.title, 'test')
