from django.db import models


class Project(models.Model):
    """
    Model representing a portfolio project. Each project contains general information,
    public and private URLs, and can be linked to multiple folders.
    """
    title = models.CharField(max_length=100, help_text="Title of the project.")
    description = models.TextField(help_text="Detailed description of the project.")
    date = models.DateField(help_text="Date of project completion or start date.")
    technologies = models.CharField(max_length=200, help_text="Comma-separated list of technologies used.")
    public_url = models.URLField(blank=True, null=True, help_text="Public link, e.g., GitHub or live demo.")
    private_url = models.URLField(blank=True, null=True, help_text="Private link, e.g., Google Drive or restricted resource.")
    is_public = models.BooleanField(default=True, help_text="Flag to indicate if project is publicly visible.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Folder(models.Model):
    """
    Model representing a folder within a project. Each folder contains related files
    and groups files by type (e.g., Documentation, Reports).
    """
    project = models.ForeignKey(Project, related_name='folders', on_delete=models.CASCADE,
                                help_text="The project to which this folder belongs.")
    name = models.CharField(max_length=100, help_text="Name of the folder, e.g., 'Documentation'.")

    def __str__(self):
        return f"{self.project.title} - {self.name}"

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"


class File(models.Model):
    """
    Model representing a file within a folder. Each file has a name, file content,
    and an option to be marked as private.
    """
    folder = models.ForeignKey(Folder, related_name='files', on_delete=models.CASCADE,
                               help_text="The folder to which this file belongs.")
    name = models.CharField(max_length=100, help_text="Name of the file, e.g., 'Project_Plan.pdf'.")
    file = models.FileField(upload_to='project_files/', help_text="File to be uploaded for the project.")
    is_private = models.BooleanField(default=False, help_text="Flag to indicate if the file is private.")

    def __str__(self):
        return f"{self.folder.name} - {self.name}"

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"
