from django.test import TestCase
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from product.views import *
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_edit_url(self):
        url=reverse("edit")
        print(resolve(url))
        self.assertEquals(resolve(url).func,product_edit)

    def test_case_delete_url(self):
        url=reverse("delete",args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func,product_delete)