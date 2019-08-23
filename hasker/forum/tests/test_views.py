from django.test import TestCase
from ..models import Question
from account.models import Person
from django.shortcuts import reverse
from random import randint


class TestForumViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        for i in range(11):
            test_user = Person.objects.create_user(
                username=f'testuser{i}',
                email=f'testuser{i}mail@mail.ru',
                password=f'123testuser{i}qwe'
            )
            test_user.save()
            
        for i in range(22):
            Question.objects.create(
                title=f'test question title {i}',
                content=f'this is test question body {i}',
                author=Person.objects.get(id=randint(1, 11))
            )
    
    def test_get_index_code(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        
    def test_index_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertTemplateUsed(resp, 'forum/index.html')

    def test_index_paginate_is_twenty(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(len(resp.context['questions']) == 20)
        
    def test_create_reply(self):
        self.client.login(username='testuser1', password='123testuser1qwe')
        q = Question.objects.get(id=randint(1, 22))
        p = Person.objects.get(id=randint(1, 11))
        data = {'related_q': q, 'body': 'some reply body', 'author': p}
        self.client.post(reverse('add_reply', kwargs={'slug': q.slug}), data)
        self.assertTrue(q.replies.count() == 1)
        
        
