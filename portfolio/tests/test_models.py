from django.test import TestCase
from django.utils import timezone
from ..models import Project, Folder, File


class ProjectModelTest(TestCase):
    def setUp(self):
        """Set up a project, folder, and file for testing model relationships."""
        self.project = Project.objects.create(
            title="Sample Project",
            description="A test project for testing purposes.",
            date=timezone.now().date(),
            technologies="Django, JavaScript, React",
            public_url="https://github.com/example/sample-project",
            private_url="https://drive.google.com/example-private",
            is_public=True
        )
        self.folder = Folder.objects.create(project=self.project, name="Documentation")
        self.file = File.objects.create(folder=self.folder, name="Project_Document.pdf", is_private=False)

    def test_project_creation(self):
        self.assertEqual(self.project.title, "Sample Project")

    def test_folder_creation(self):
        self.assertEqual(self.folder.name, "Documentation")
        self.assertEqual(self.folder.project, self.project)

    def test_file_creation(self):
        self.assertEqual(self.file.name, "Project_Document.pdf")
        self.assertEqual(self.file.folder, self.folder)
        self.assertFalse(self.file.is_private)
