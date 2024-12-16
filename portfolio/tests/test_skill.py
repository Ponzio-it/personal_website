# portfolio/tests.py

from django.test import TestCase
from django.urls import reverse
from ..models import Skill, Certificate, Education


class SkillTests(TestCase):
    """Tests for Skill functionality on the education page."""

    def setUp(self):
        # Create skills
        self.skill_python = Skill.objects.create(name_en="Python", name_it="Python")
        self.skill_data_analysis = Skill.objects.create(name_en="Data Analysis", name_it="Analisi dei dati")

        # Create certificates and link to skills
        self.certificate_python = Certificate.objects.create(
            title_en="Python Certification",
            title_it="Certificazione Python",
            description_en="Certificate for Python programming.",
            description_it="Certificato per la programmazione Python.",
            link="http://example.com/python"
        )
        self.certificate_python.skills.add(self.skill_python)

        self.certificate_data_analysis = Certificate.objects.create(
            title_en="Data Analysis Certification",
            title_it="Certificazione Analisi dei Dati",
            description_en="Certificate for Data Analysis.",
            description_it="Certificato per l'analisi dei dati.",
            link="http://example.com/data-analysis"
        )
        self.certificate_data_analysis.skills.add(self.skill_data_analysis)

        # Create education entries and link to skills
        self.education_cs = Education.objects.create(
            institution_en="University of Test",
            institution_it="Università di Test",
            degree="Bachelors",
            field_of_study_en="Computer Science",
            field_of_study_it="Informatica",
            start_date="2017-01-01",
            end_date="2021-01-01",
            description_en="Bachelor's degree in Computer Science.",
            description_it="Laurea in Informatica."
        )
        self.education_cs.skills.add(self.skill_python)

        self.education_data_sci = Education.objects.create(
            institution_en="University of Test",
            institution_it="Università di Test",
            degree="Masters",
            field_of_study_en="Data Science",
            field_of_study_it="Scienza dei Dati",
            start_date="2021-01-01",
            end_date="2023-01-01",
            description_en="Master's degree in Data Science.",
            description_it="Master in Scienza dei Dati."
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
        """Test that filtering by skill displays only the relevant certificates and education entries."""
        # Filter by Python skill
        response = self.client.get(self.education_url, {'skill': self.skill_python.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Certification")
        self.assertContains(response, "Computer Science")
        self.assertNotContains(response, "Data Analysis Certification")
        self.assertNotContains(response, "Data Science")

        # Filter by Data Analysis skill
        response = self.client.get(self.education_url, {'skill': self.skill_data_analysis.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Data Analysis Certification")
        self.assertContains(response, "Data Science")
        self.assertNotContains(response, "Python Certification")
        self.assertNotContains(response, "Computer Science")

    def test_no_filter_displays_all_certificates_and_education(self):
        """Test that without a filter, all certificates and education entries are displayed."""
        response = self.client.get(self.education_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Certification")
        self.assertContains(response, "Data Analysis Certification")
        self.assertContains(response, "Computer Science")
        self.assertContains(response, "Data Science")
