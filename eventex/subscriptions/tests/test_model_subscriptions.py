from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Eduardo Caetano Sousa',
            cpf='05523258196',
            email='caetasousa@gmail.com',
            phone='62-99969-7481'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        '''Subscription must have on auto created_at attr'''
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Eduardo Caetano Sousa', str(self.obj))

    def test_default_to_false(self):
        '''By default paid must be false'''
        self.assertEqual(False, self.obj.paid)