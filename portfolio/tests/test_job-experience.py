from django.urls import reverse
from django.test import TestCase
from ..models import Skill, Certificate, Education, JobExperience

class EducationViewTests(TestCase):
    def setUp(self):
        # Set up skills, certificates, education entries, and job experiences
        self.skill_python = Skill.objects.create(name="Python")
        
        self.certificate_python = Certificate.objects.create(title="Python Certification", description="Python course")
        self.certificate_python.skills.add(self.skill_python)

        self.education_cs = Education.objects.create(institution="University of Test", degree="Bachelor's", field_of_study="Computer Science", start_date="2018-01-01", end_date="2022-01-01", description="Bachelor degree in Computer Science.")
        self.education_cs.skills.add(self.skill_python)

        self.job_python = JobExperience.objects.create(title="Software Developer", company="Tech Co", start_date="2021-06-01", end_date=None, description="Developed software using Python.")
        self.job_python.skills.add(self.skill_python)

        self.education_url = reverse('portfolio:education')

    def test_filter_by_skill(self):
        # Test filtering by Python skill
        response = self.client.get(self.education_url, {'skill': self.skill_python.id})
        self.assertContains(response, "Python Certification")
        self.assertContains(response, "Bachelor&#x27;s in Computer Science")
        self.assertContains(response, "Software Developer at Tech Co")
