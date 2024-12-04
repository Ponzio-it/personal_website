from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from ..models import Project, Folder, File
from unittest.mock import patch


class ProjectViewTests(TestCase):
    """Test case for views related to the portfolio project."""

    def setUp(self):
        """Set up a sample public project for testing views."""
        self.project = Project.objects.create(
            title="Sample Project",
            description="A test project for testing views.",
            date=timezone.now().date(),
            technologies="Python, Django",
            public_url="https://github.com/example/sample-project",
            is_public=True
        )
        self.folder = Folder.objects.create(
            project=self.project,
            name="Docs"
        )
        self.file = File.objects.create(
            folder=self.folder,
            name="Project_Guide.pdf",
            is_private=True
        )

    def test_projects_view_status_code(self):
        """Test if the projects view is accessible and returns status code 200."""
        response = self.client.get(reverse('portfolio:projects'))
        self.assertEqual(response.status_code, 200)

    def test_projects_view_template_used(self):
        """Test if the projects view uses the correct template."""
        response = self.client.get(reverse('portfolio:projects'))
        self.assertTemplateUsed(response, 'portfolio/projects.html')

    def test_projects_view_context_data(self):
        """Test if the projects view returns the correct context data."""
        response = self.client.get(reverse('portfolio:projects'))
        projects = response.context['projects']
        self.assertIn(self.project, projects)
        # Check folder and file existence in project
        self.assertIn(self.folder, self.project.folders.all())
        self.assertIn(self.file, self.folder.files.all())

    def test_home_view_status_code(self):
        """Test if the home view is accessible."""
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_me_view_status_code(self):
        """Test if the education view is accessible."""
        response = self.client.get(reverse('portfolio:education'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_status_code(self):
        """Test if the contact view is accessible."""
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)

    @patch('portfolio.views.open', side_effect=FileNotFoundError)
    def test_open_cv_view_status_code(self, mock_open):
        """Test if the open_cv view is accessible and handles missing file gracefully."""
        response = self.client.get(reverse('portfolio:open_cv'))
        # Assuming the file does not exist, expect a 404
        self.assertEqual(response.status_code, 404)