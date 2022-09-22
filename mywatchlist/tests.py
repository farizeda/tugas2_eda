from django.test import TestCase, Client 
from django.urls import reverse

# Create your tests here.
class PageTesting(TestCase):
    def test_html_exist_showed(self):
        response = Client().get(reverse ('mywatchlist:show_watchlist')) 
        self.assertEqual(response.status_code, 200)

    def test_xml_exist_showed(self):
        response = Client().get(reverse('mywatchlist:show_xml')) 
        self.assertEqual(response.status_code, 200)

    def test_ison_exist_showed(self):
        response = Client().get(reverse('mywatchlist:show_json')) 
        self.assertEqual(response.status_code, 200)