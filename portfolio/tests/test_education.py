# portfolio/tests.py

from django.test import TestCase
from django.urls import reverse
from ..models import Certificate, Education

class EducationPageTests(TestCase):
    def setUp(self):
        self.url = reverse('portfolio:education')

    def test_education_page_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_education_page_with_no_data(self):
        response = self.client.get(self.url)
        self.assertContains(response, "No certificates available.")
        self.assertContains(response, "No educational background available.")

    def test_education_page_with_data(self):
        # Create sample data
        Certificate.objects.create(
            title="Sample Certificate",
            description="A sample certificate description.",
            link="http://example.com"
        )
        Education.objects.create(
            institution="Sample University",
            degree="Masters",
            field_of_study="Computer Science",
            start_date="2020-01-01",
            end_date="2022-01-01",
            description="A sample master's program."
        )

        response = self.client.get(self.url)
        
        # Check if the created data appears on the page
        self.assertContains(response, "Sample Certificate")
        self.assertContains(response, "Sample University")
