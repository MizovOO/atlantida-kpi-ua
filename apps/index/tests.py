from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):

    def test_index_general(self):
        """
        Index page should exist
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
