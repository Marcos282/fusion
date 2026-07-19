from django.test import SimpleTestCase
from django.urls import reverse


class IndexViewTests(SimpleTestCase):
    def test_home_page_renders_index_template(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
