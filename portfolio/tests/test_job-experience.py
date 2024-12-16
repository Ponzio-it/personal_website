from django.urls import reverse
from django.test import TestCase
from portfolio.models import Skill, Certificate, Education, JobExperience


class EducationViewTests(TestCase):
    def setUp(self):
        """Set up skills, certificates, education entries, and job experiences for testing the Education view."""
        self.skill_python = Skill.objects.create(name_en="Python", name_it="Python")
        
        self.certificate_python = Certificate.objects.create(
            title_en="Python Certification", 
            title_it="Certificazione Python", 
            description_en="Python course", 
            description_it="Corso di Python"
        )
        self.certificate_python.skills.add(self.skill_python)

        self.education_cs = Education.objects.create(
            institution_en="University of Test", 
            institution_it="Università di Test", 
            degree="Bachelor's", 
            field_of_study_en="Computer Science", 
            field_of_study_it="Informatica", 
            start_date="2018-01-01", 
            end_date="2022-01-01", 
            description_en="Bachelor degree in Computer Science.", 
            description_it="Laurea in Informatica."
        )
        self.education_cs.skills.add(self.skill_python)

        self.job_python = JobExperience.objects.create(
            title_en="Software Developer", 
            title_it="Sviluppatore Software", 
            company="Tech Co", 
            start_date="2021-06-01", 
            end_date=None, 
            description_en="Developed software using Python.", 
            description_it="Sviluppato software utilizzando Python."
        )
        self.job_python.skills.add(self.skill_python)

        self.education_url = reverse('portfolio:education')

    def test_filter_by_skill(self):
        """Test filtering by Python skill displays relevant certificates, education, and job experiences."""
        response = self.client.get(self.education_url, {'skill': self.skill_python.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Certification")
        self.assertContains(response, "Bachelor's")
        self.assertContains(response, "Software Developer at Tech Co")
