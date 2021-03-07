from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Eduardo Caetano Sousa', cpf='05523258196',
                    email='caetasousa@gmail.com', phone='62-99969-7481')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'caetasousa@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['caetasousa@gmail.com', 'caetasousa@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Eduardo Caetano Sousa',
                    '05523258196',
                    'caetasousa@gmail.com',
                    '62-99969-7481'
                    ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
