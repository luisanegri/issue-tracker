from django.test import TestCase
from .models import Issue

# Create your tests here.

class IssueTests(TestCase):
    def test_title(self):
        test_title = Issue(title="A bug")
        self. assertEqual(str(test_title), "A bug")