# portfolio/tests.py

from django.test import TestCase
from django.urls import reverse
from portfolio.models import Certificate, Education


class EducationPageTests(TestCase):
    def setUp(self):
        """Set up the URL for the education page."""
        self.url = reverse('portfolio:education')

    def test_education_page_status_code(self):
        """Test that the education page returns a 200 status code."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_education_page_with_no_data(self):
        """Test that the education page displays the correct message when there is no data."""
        response = self.client.get(self.url)
        self.assertContains(response, "No certificates available.")
        self.assertContains(response, "No educational background available.")

    def test_education_page_with_data(self):
        """Test that the education page displays certificates and education data if available."""
        # Create sample data
        Certificate.objects.create(
            title_en="Sample Certificate", 
            title_it="Certificato di esempio", 
            description_en="A sample certificate description.", 
            description_it="Descrizione di un certificato di esempio.", 
            link="http://example.com"
        )
        Education.objects.create(
            institution_en="Sample University", 
            institution_it="Università di esempio", 
            degree="Masters", 
            field_of_study_en="Computer Science", 
            field_of_study_it="Informatica", 
            start_date="2020-01-01", 
            end_date="2022-01-01", 
            description_en="A sample master's program.", 
            description_it="Un programma di master di esempio."
        )

        response = self.client.get(self.url)
        
        # Check if the created data appears on the page
        self.assertContains(response, "Sample Certificate")
        self.assertContains(response, "Sample University")
