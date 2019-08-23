from django.test import TestCase
from ..models import Person
from django.shortcuts import reverse


class TestLogin(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        for i in range(2):
            test_user = Person.objects.create_user(
                username=f'testuser{i}',
                email=f'testuser{i}mail@mail.ru',
                password=f'123testuser{i}qwe'
            )
            test_user.save()
        
    def test_redirect_freeinfo_if_not_logged_in(self):
        resp = self.client.get(reverse('person_info', kwargs={'nickname': 'testuser'}))
        self.assertRedirects(resp, reverse('login') + '?next=%2Fhasker%2Faccount%2Ftestuser%2F')

    def test_redirect_profile_if_not_logged_in(self):
        resp = self.client.get(reverse('person_profile'))
        self.assertRedirects(resp, reverse('login') + '?next=/hasker/account/profile/')
        
    def test_login(self):
        self.client.login(username='testuser1', password='123testuser1qwe')
        resp = self.client.get(reverse('person_profile'))
        self.assertEqual(str(resp.context['user']), 'testuser1 <testuser1mail@mail.ru>')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'account/_profile.html')
        

        