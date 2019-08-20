from django.test import TestCase
from ..models import Question, Reply
from account.models import Person


class QuestionTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        p1 = Person.objects.create(
            username='testuser',
            email='testusermail@mail.ru',
            password='123testuserqwe'
        )
        p2 = Person.objects.create(
            username='testuser2',
            email='testuser2mail@mail.ru',
            password='123testuser2qwe'
        )
        q = Question.objects.create(
            title='test question title',
            content='this is test question body',
            author=p1
        )
        Reply.objects.create(
            related_q=q,
            body='that is first reply',
            author=p2
        )
        
    def test_question_exists(self):
        q = Question.objects.get(id=1)
        self.assertTrue(isinstance(q, Question))

    def test_reply_exists(self):
        r = Reply.objects.get(id=1)
        self.assertTrue(isinstance(r, Reply))
