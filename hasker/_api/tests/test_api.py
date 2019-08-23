from tastypie.test import ResourceTestCaseMixin
from django.test import TestCase


class EntryResourceTest(ResourceTestCaseMixin, TestCase):

    def test_get_questions_valid_json(self):
        resp = self.api_client.get('/hasker/api/questions/', format='json')
        self.assertValidJSONResponse(resp)

