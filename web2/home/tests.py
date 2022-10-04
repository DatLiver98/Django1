#ktra app 
from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        response = self.client.get('/') #goi path('', include('home.urls')), neu ok 200, nook 404
        self.assertEquals(response.status_code, 200) # so sanh xem status co = 200?