from django.test import TestCase

from app.models import Location

# Create your tests here.
class LocationTestCase(TestCase):
	def setUp(self):
		Location.objects.create(name="Test Location")

	def test_location_name(self):
		location = Location.objects.get(name="Test Location")
		self.assertEqual(location.name, "Test Location")

	def test_location_str(self):
		location = Location.objects.get(name="Test Location")
		self.assertEqual(str(location), "Test Location")
		