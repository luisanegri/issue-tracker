from django.test import TestCase
from .models import Issue

# Create your tests here.

class IssueTests(TestCase):
    def test_name(self):
        test_name = Issue(name="A bug")
        self. assertEqual(str(test_name), "A bug")