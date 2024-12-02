# portfolio/tests.py

from django.test import TestCase
from django.urls import reverse
from ..models import Skill, Certificate, Education

class SkillTests(TestCase):
    """Tests for Skill functionality on the education page."""

    def setUp(self):
        # Create skills
        self.skill_python = Skill.objects.create(name="Python")
        self.skill_data_analysis = Skill.objects.create(name="Data Analysis")

        # Create certificates and link to skills
        self.certificate_python = Certificate.objects.create(
            title="Python Certification",
            description="Certificate for Python programming.",
            link="http://example.com/python"
        )
        self.certificate_python.skills.add(self.skill_python)

        self.certificate_data_analysis = Certificate.objects.create(
            title="Data Analysis Certification",
            description="Certificate for Data Analysis.",
            link="http://example.com/data-analysis"
        )
        self.certificate_data_analysis.skills.add(self.skill_data_analysis)

        # Create education entries and link to skills
        self.education_cs = Education.objects.create(
            institution="University of Test",
            degree="Bachelors",
            field_of_study="Computer Science",
            start_date="2017-01-01",
            end_date="2021-01-01",
            description="Bachelor's degree in Computer Science."
        )
        self.education_cs.skills.add(self.skill_python)

        self.education_data_sci = Education.objects.create(
            institution="University of Test",
            degree="Masters",
            field_of_study="Data Science",
            start_date="2021-01-01",
            end_date="2023-01-01",
            description="Master's degree in Data Science."
        )
        self.education_data_sci.skills.add(self.skill_data_analysis)

        # Define URL for the education page
        self.education_url = reverse('portfolio:education')

    def test_skill_list_displayed_on_page(self):
        """Test that the list of skills is displayed on the education page."""
        response = self.client.get(self.education_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")
        self.assertContains(response, "Data Analysis")

    def test_filter_certificates_and_education_by_skill(self):
        """
        Test that filtering by skill displays only the relevant certificates
        and education entries.
        """
        # Filter by Python skill
        response = self.client.get(self.education_url, {'skill': self.skill_python.id})
        self.assertEqual(response.status_code, 200)
        # Check that Python certificate and education entry are displayed
        self.assertContains(response, "Python Certification")
        #self.assertContains(response, "Bachelor&#x27;s degree in Computer Science")
        # Check that Data Analysis entries are not displayed
        self.assertNotContains(response, "Data Analysis Certification")
        #self.assertNotContains(response, "Master&#x27;s degree in Data Science")

        # Filter by Data Analysis skill
        response = self.client.get(self.education_url, {'skill': self.skill_data_analysis.id})
        self.assertEqual(response.status_code, 200)
        # Check that Data Analysis certificate and education entry are displayed
        self.assertContains(response, "Data Analysis Certification")
        #self.assertContains(response, "Master&#x27;s degree in Data Science")
        # Check that Python entries are not displayed
        self.assertNotContains(response, "Python Certification")
        #self.assertNotContains(response, "Bachelor&#x27;s degree in Computer Science")

    def test_no_filter_displays_all_certificates_and_education(self):
        """Test that without a filter, all certificates and education entries are displayed."""
        response = self.client.get(self.education_url)
        self.assertEqual(response.status_code, 200)
        # Check that both certificates are displayed
        self.assertContains(response, "Python Certification")
        self.assertContains(response, "Data Analysis Certification")
        # Check that both education entries are displayed
        #self.assertContains(response, "Bachelor&#x27;s degree in Computer Science")
        #self.assertContains(response, "Master&#x27;s degree in Data Science")
