from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionsFormTest(TestCase):
    def tests_form_has_fields(self):
        '''Form must have 4 fields'''
        expected = ['name', 'cpf', 'email', 'phone']
        form = SubscriptionForm()
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        '''CPF must only accpet digits'''
        form = self.make_validate_form(cpf='AAA23258196')
        self.assertListEqual(['cpf'], list(form.errors))

    def test_cpf_has_11_digits(self):
        form = self.make_validate_form(cpf='5196')
        self.assertListEqual(['cpf'], list(form.errors))

    def test_name_must_be_capitalized(self):
        form = self.make_validate_form(name='EDUARDO caetano')
        self.assertEqual('Eduardo Caetano', form.cleaned_data['name'])

    def make_validate_form(self, **kwargs):
        valid = dict(name='Eduardo Caetano Sousa', cpf='04423258196',
                     email='caetasousa@gmail.com', phone='62-99969-7481')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def test_email_is_optional(self):
        form = self.make_validate_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        form = self.make_validate_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        form = self.make_validate_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))
