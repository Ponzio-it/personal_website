# portfolio/tests.py

from django.test import TestCase
from django.urls import reverse
from ..models import ContactInfo

class ContactPageTests(TestCase):
    """Test cases for the contact page."""

    def setUp(self):
        """
        Setup a test client and optionally create a ContactInfo instance
        to be used in multiple tests.
        """
        self.contact_url = reverse('portfolio:contact')  # Assuming 'contact' is the name of the URL

    def test_contact_page_without_contact_info(self):
        """
        Test the contact page when there is no contact information available.
        The page should display a message indicating the lack of contact information.
        """
        response = self.client.get(self.contact_url)
        
        # Check that the page loads correctly with a 200 status code
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'portfolio/contact.html')
        
        # Check that the 'not available' message is displayed
        self.assertContains(response, "Contact information is currently unavailable.")

    def test_contact_page_with_contact_info(self):
        """
        Test the contact page when contact information is available.
        The page should display the email, LinkedIn, and GitHub information.
        """
        # Create a ContactInfo instance
        ContactInfo.objects.create(
            email='test@example.com',
            linkedin_url='https://www.linkedin.com/in/testuser/',
            github_url='https://github.com/testuser'
        )

        response = self.client.get(self.contact_url)

        # Check that the page loads correctly with a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check that the contact information is correctly rendered on the page
        self.assertContains(response, 'test@example.com')
        self.assertContains(response, 'https://www.linkedin.com/in/testuser/')
        self.assertContains(response, 'https://github.com/testuser')
        
        # Check that mailto link is correctly rendered
        self.assertContains(response, 'mailto:test@example.com')

    def test_contact_page_template_used(self):
        """
        Ensure the contact page uses the correct template.
        """
        response = self.client.get(self.contact_url)
        self.assertTemplateUsed(response, 'portfolio/contact.html')
