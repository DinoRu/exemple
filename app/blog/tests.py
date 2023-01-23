import unittest
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class IndexPageTest(TestCase):
	def test_index_page(self):
		response = self.client.get(reverse('blog:home'))
		self.assertEqual(response.status_code, 200)

class TestSimpleComponent(TestCase):
	def test_basic_sum(self):
		assert 1 + 1 == 2
		
