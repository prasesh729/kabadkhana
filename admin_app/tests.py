from django.test import TestCase
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from admin_app.views import *

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_admindashboard_url(self):
        url=reverse("dashboard")
        print(resolve(url))
        self.assertEquals(resolve(url).func,admindashboard)

    def test_case_addadmin_url(self):
        url=reverse("addadmin")
        print(resolve(url))
        self.assertEquals(resolve(url).func,addadmins)

    def test_case_C_details_url(self):
        url=reverse("customers")
        print(resolve(url))
        self.assertEquals(resolve(url).func,C_details)

    def test_case_login_url(self):
        url=reverse("login")
        print(resolve(url))
        self.assertEquals(resolve(url).func,adminlogin)

    def test_case_logout_url(self):
        url=reverse("logout")
        print(resolve(url))
        self.assertEquals(resolve(url).func,signout)

    def test_case_products_url(self):
        url=reverse("products")
        print(resolve(url))
        self.assertEquals(resolve(url).func,p_details)