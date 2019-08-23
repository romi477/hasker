from django.test import TestCase
from ..models import Question, Reply
from account.models import Person


class ForumModelsTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        asker = Person.objects.create(
            username='testuser',
            email='testusermail@mail.ru',
            password='123testuserqwe'
        )
        replier = Person.objects.create(
            username='testuser2',
            email='testuser2mail@mail.ru',
            password='123testuser2qwe'
        )
        quest = Question.objects.create(
            title='test question title',
            content='this is test question body',
            author=asker
        )
        Reply.objects.create(
            related_q=quest,
            body='that is first reply',
            author=replier
        )
        
    def test_question_exists(self):
        q = Question.objects.get(id=1)
        self.assertTrue(isinstance(q, Question))

    def test_reply_exists(self):
        r = Reply.objects.get(id=1)
        self.assertTrue(isinstance(r, Reply))
