from django.test import TestCase
from ..forms import QuestionForm


class TestQuestionForm(TestCase):
    
    def test_question_valid_form(self):
        data = {
            'title': 'some title',
            'content': 'some content',
            'tags': 'tag1, tag2, tag3'
        }
        form = QuestionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_question_invalid_form_title_more_than_255_characters(self):
        data = {
            'title': 'Testing is vital. Without properly testing your code, '
                     'you will never know if the code works as it should, now '
                     'or in the future when the codebase changes. Countless hours '
                     'can be lost fixing problems caused by changes to the codebase. '
                     'What’s worse, you may not even know',
            'content': 'some content',
            'tags': 'tag1, tag2, tag3'
        }
        form = QuestionForm(data=data)
        self.assertFalse(form.is_valid())
