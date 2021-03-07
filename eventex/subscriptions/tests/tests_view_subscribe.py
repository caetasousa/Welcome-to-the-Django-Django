from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        '''Get /inscricao/ must return status code 200'''
        self.assertEqual(200, self.resp.status_code)

    def test_templates(self):
        '''Must use subscriptions/subscriptions_form.html'''
        self.assertTemplateUsed(self.resp, 'subscriptions/subscriptions_form.html')

    def tests_html(self):
        '''Html must contain tags'''
        tags = (('<form', 1), ('<input', 6), ('type="text"', 3), ('type="email"', 1), ('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        '''Context must have subscription form'''
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Eduardo Caetano Sousa', cpf='05523258196',
                    email='caetasousa@gmail.com', phone='62-99969-7481')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        '''Valid Post shoud redirect to /inscricao/'''
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))


    def test_save_subscrition(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        '''Invalid Post should not redirect'''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscriptions_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscrition(self):
        self.assertFalse(Subscription.objects.exists())


class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict(name='Eduardo Caetano Sousa', cpf='05523258196',
                email='caetasousa@gmail.com', phone='62-99969-7481')
        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')