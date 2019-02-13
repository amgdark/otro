from django.test import TestCase

# Create your tests here.

class TestArticulos(TestCase):
	
    def test_smoke(self):
        self.assertEquals(2,2)
