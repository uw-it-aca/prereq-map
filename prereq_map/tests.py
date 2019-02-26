from django.test import TestCase, Client


class TestView(TestCase):
    def test_page_view(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 302)
