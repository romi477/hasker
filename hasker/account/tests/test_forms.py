from django.test import TestCase
from ..forms import PersonForm


class TestUserForm(TestCase):
    
    def test_valid_registration_form(self):
        data = {
            'username': 'testuser3',
            'email': 'testuser3@mail.ru',
            'password1': '123testuser3qwerty',
            'password2': '123testuser3qwerty'
        }
        form = PersonForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        data = {
            'username': 'testuser3',
            'email': 'testuser3@mail.ru',
            'password1': '123testuser3qwerty',
            'password2': ''
        }
        form = PersonForm(data=data)
        self.assertFalse(form.is_valid())

        