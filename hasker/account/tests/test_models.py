from django.test import TestCase
from ..models import Person


class PersonTest(TestCase):
    
    @staticmethod
    def create_person():
        return Person.objects.create(
            username='testuser',
            email='testusermail@mail.ru',
            password='123testuserqwe'
        )
    
    def test_person_creation(self):
        p = self.create_person()
        self.assertTrue(isinstance(p, Person))
    
    def test_getting_avatar(self):
        p = self.create_person()
        self.assertEqual(p.get_ava(), 'avatars/def_ava.jpg')
      