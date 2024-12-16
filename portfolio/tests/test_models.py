from django.test import TestCase
from django.utils import timezone
from portfolio.models import Project


class ProjectModelTest(TestCase):
    def setUp(self):
        """Set up a project for testing the Project model."""
        self.project = Project.objects.create(
            title_en="Sample Project",
            title_it="Progetto di esempio",
            description_en="A test project for testing purposes.",
            description_it="Un progetto di test per scopi di test.",
            date=timezone.now().date(),
            technologies="Django, JavaScript, React",
            public_url="https://github.com/example/sample-project",
            private_url="https://drive.google.com/example-private",
            is_public=True
        )

    def test_project_creation(self):
        """Test that a project is created with correct field values."""
        self.assertEqual(self.project.title_en, "Sample Project")
        self.assertEqual(self.project.description_en, "A test project for testing purposes.")
        self.assertTrue(self.project.is_public)