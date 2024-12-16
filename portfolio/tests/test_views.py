from django.test import TestCase, Client
from django.urls import reverse
from ..models import (
    Project,ContactInfo, Skill, Certificate, 
    Education,
)


class EducationViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('portfolio:education')
        self.skill = Skill.objects.create(name_en='Python', name_it='Python')
        self.certificate = Certificate.objects.create(
            title_en='Test Certificate',
            title_it='Certificato di Test',
            description_en='Test description',
            description_it='Descrizione di test',
            link='http://example.com'
        )
        self.certificate.skills.add(self.skill)
        self.education = Education.objects.create(
            institution_en='Test University',
            institution_it='Università di Test',
            degree='Bachelors',
            field_of_study_en='Computer Science',
            field_of_study_it='Informatica',
            start_date='2020-01-01',
            end_date='2024-01-01'
        )
        self.education.skills.add(self.skill)

    def test_education_view_renders_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/education.html')

    def test_education_view_context_contains_expected_data(self):
        response = self.client.get(self.url)
        self.assertIn('skills', response.context)
        self.assertIn('certificates', response.context)
        self.assertIn('education_history', response.context)


class ProjectsViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('portfolio:projects')
        self.project = Project.objects.create(
            title_en='Test Project',
            title_it='Progetto di Test',
            description_en='Project description',
            description_it='Descrizione del progetto',
            date='2024-01-01',
            technologies='Python, Django',
            public_url='http://example.com',
            is_public=True
        )

    def test_projects_view_renders_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/projects.html')

    def test_projects_view_context_contains_expected_data(self):
        response = self.client.get(self.url)
        self.assertIn('projects', response.context)


class ContactViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('portfolio:contact')
        self.contact_info = ContactInfo.objects.create(email='test@example.com')

    def test_contact_view_renders_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/contact.html')

    def test_contact_view_post_valid_form_sends_email_and_renders_success_message(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'success')

    #def test_contact_view_post_invalid_form_renders_form_with_errors(self):
     #   data = {'first_name': '', 'email': ''}  # Missing required fields
      #  response = self.client.post(self.url, data)
       # self.assertEqual(response.status_code, 200)
        #self.assertFormError(response, 'form', 'last_name', 'This field is required.')
         #self.assertFormError(response, 'form', 'message', 'This field is required.')
