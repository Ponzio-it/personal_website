from django.db import models
from django.core.exceptions import ValidationError #use in ContactInfo
from django.utils.text import slugify #use in Category

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
    project = models.ForeignKey(Project, related_name='folders', on_delete=models.CASCADE, help_text="The project to which this folder belongs.")
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
    folder = models.ForeignKey(Folder, related_name='files', on_delete=models.CASCADE, help_text="The folder to which this file belongs.")
    name = models.CharField(max_length=100, help_text="Name of the file, e.g., 'Project_Plan.pdf'.")
    file = models.FileField(upload_to='project_files/', help_text="File to be uploaded for the project.")
    is_private = models.BooleanField(default=False, help_text="Flag to indicate if the file is private.")

    def __str__(self):
        return f"{self.folder.name} - {self.name}"

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

class ContactInfo(models.Model):
    """Model to store site-wide contact information."""

    email = models.EmailField(help_text="Email address for contacting the site owner.")

    def __str__(self):
        """Return the email as the string representation."""
        return self.email

    def save(self, *args, **kwargs):
        """
        Ensure only one instance of ContactInfo exists.
        This prevents the creation of multiple instances in the database.
        """
        if not self.pk and ContactInfo.objects.exists():
            raise ValidationError('Only one instance of ContactInfo is allowed.')
        super(ContactInfo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'


class Skill(models.Model):
    """Model to represent a skill that can be linked to certificates and education entries."""
    name = models.CharField(max_length=100, unique=True, help_text="The name of the skill (e.g., Python, Data Analysis).")

    def __str__(self):
        return self.name


class Certificate(models.Model):
    """Model to store certificates with links to descriptions and course information."""
    title = models.CharField(max_length=255, help_text="The title of the certificate.")
    description = models.TextField(help_text="Description of the course.")
    link = models.URLField(help_text="URL to the certificate or course information.")
    skills = models.ManyToManyField(Skill, related_name="certificates", blank=True, help_text="Skills related to this certificate.")

    def __str__(self):
        return self.title

class Education(models.Model):
    """Model to store educational background information, such as university and master’s degrees."""
    DEGREE_CHOICES = [
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('PhD', 'PhD'),
        ('Other', 'Other'),
    ]
    
    institution = models.CharField(max_length=255, help_text="Name of the educational institution.")
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, help_text="Degree type (e.g., Bachelor's, Master's).")
    field_of_study = models.CharField(max_length=255, help_text="Field of study (e.g., Computer Science).")
    start_date = models.DateField(help_text="Start date of the program.")
    end_date = models.DateField(help_text="End date of the program, or expected end date.")
    description = models.TextField(blank=True, help_text="Optional description of the program or notable achievements.")
    skills = models.ManyToManyField(Skill, related_name="educations", blank=True, help_text="Skills related to this educational entry.")
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"

class Review(models.Model):
    """
    Model for storing user reviews associated with a project.
    Reviews are created by users and are subject to admin approval.
    """

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    project = models.ForeignKey('Project', related_name='reviews', on_delete=models.CASCADE, help_text="The project this review is associated with.")
    reviewer_name = models.CharField(max_length=100,help_text="Name of the reviewer submitting the review.")
    content = models.TextField(help_text="Content of the review.")
    recommendation = models.BooleanField(default=False,help_text="Does the reviewer recommend this project?")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending', help_text="Approval status of the review.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp for when the review was created.")

    def __str__(self):
        return f"Review by {self.reviewer_name} on {self.project.title}"

class JobExperience(models.Model):
    """Model to represent a job experience entry associated with various skills."""
    
    title = models.CharField(max_length=255, help_text="Job title (e.g., Software Developer)")
    company = models.CharField(max_length=255, help_text="Company name")
    start_date = models.DateField(help_text="Start date of the job")
    end_date = models.DateField(null=True, blank=True, help_text="End date of the job (if applicable)")
    description = models.TextField(blank=True, help_text="Description of responsibilities or achievements")
    skills = models.ManyToManyField(Skill, related_name="job_experiences", blank=True, help_text="Skills related to this job experience")

    def __str__(self):
        return f"{self.title} at {self.company}"


class Section(models.Model):
    """Model to represent personal description"""

    title = models.CharField(max_length=200, help_text="Title of the section")
    description = models.TextField(help_text="Description content for the section")

    def __str__(self):
        return self.title
    

class Category(models.Model):
    """
    Model representing a blog category.

    Attributes:
        name (str): The name of the category.
        slug (str): A URL-friendly identifier for the category.
    """
    name = models.CharField(max_length=100, help_text="Name of the category.")
    slug = models.SlugField(max_length=100, unique=True, blank=True, help_text="URL-friendly identifier for the category (auto-generated).")

    def save(self, *args, **kwargs):
        """
        Automatically generate a slug from the category name if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the string representation of the category.
        """
        return self.name


class BlogPost(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (str): The title of the blog post.
        slug (str): A URL-friendly identifier for the post.
        content (str): The main content of the post.
        excerpt (str): A short summary or excerpt from the post.
        featured_image (ImageField): An optional featured image for the post.
        publication_date (date): The date the post was published.
        categories (Category): Categories associated with the post.
        author (str): The name of the post's author.
    """
    title = models.CharField(max_length=200, help_text="Title of the blog post.")
    slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="URL-friendly identifier for the post (auto-generated).")
    content = models.TextField(help_text="Main content of the blog post.")
    excerpt = models.TextField(blank=True, help_text="Short summary or excerpt of the blog post.")
    featured_image = models.ImageField(upload_to='blog_images/',blank=True, null=True, help_text="Optional featured image for the blog post.")
    publication_date = models.DateField(auto_now_add=True, help_text="Date the blog post was published.")
    categories = models.ManyToManyField(Category, related_name='blog_posts', help_text="Categories associated with the blog post.")
    author = models.CharField(max_length=100, help_text="Author of the blog post.")

    def save(self, *args, **kwargs):
        """
        Automatically generate a slug from the blog post title if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return the string representation of the blog post (its title).
        """
        return self.title