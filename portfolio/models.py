from django.db import models
from django.core.exceptions import ValidationError  # Use in ContactInfo
from django.utils.text import slugify  # Use in Category
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    """
    Model representing a portfolio project. Each project contains general information,
    public and private URLs, and can be linked to multiple folders.
    """
    title_en = models.CharField(
        max_length=100, 
        help_text=_("Title of the project in English."), 
        verbose_name=_("Title (EN)")
    )
    title_it = models.CharField(
        max_length=100, 
        help_text=_("Title of the project in Italian."), 
        verbose_name=_("Title (IT)")
    )
    description_en = models.TextField(
        help_text=_("Detailed description of the project in English."), 
        verbose_name=_("Description (EN)")
    )
    description_it = models.TextField(
        help_text=_("Detailed description of the project in Italian."), 
        verbose_name=_("Description (IT)")
    )
    date = models.DateField(
        help_text=_("Date of project completion or start date."), 
        verbose_name=_("Date")
    )
    technologies = models.CharField(
        max_length=200, 
        help_text=_("Comma-separated list of technologies used."), 
        verbose_name=_("Technologies")
    )
    public_url = models.URLField(
        blank=True, 
        null=True, 
        help_text=_("Public link, e.g., GitHub or live demo."), 
        verbose_name=_("Public URL")
    )
    private_url = models.URLField(
        blank=True, 
        null=True, 
        help_text=_("Private link, e.g., Google Drive or restricted resource."), 
        verbose_name=_("Private URL")
    )
    is_public = models.BooleanField(
        default=True, 
        help_text=_("Flag to indicate if project is publicly visible."), 
        verbose_name=_("Is Public")
    )
    google_file_id = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text=_("Google File ID for embedding a presentation."), 
        verbose_name=_("Google File ID")
    )
    onedrive_share_link = models.URLField(
        max_length=2000,
        blank=True,
        null=True,
        help_text=_("OneDrive share link for embedding a presentation"),
        verbose_name=_("OneDrive_Link")
    )
    
    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


class Folder(models.Model):
    """
    Model representing a folder within a project. Each folder contains related files
    and groups files by type (e.g., Documentation, Reports).
    """
    project = models.ForeignKey(
        'Project', 
        related_name='folders', 
        on_delete=models.CASCADE, 
        help_text=_("The project to which this folder belongs."), 
        verbose_name=_("Project")
    )
    name_en = models.CharField(
        max_length=100, 
        help_text=_("Name of the folder in English, e.g., 'Documentation'."), 
        verbose_name=_("Name (EN)")
    )
    name_it = models.CharField(
        max_length=100, 
        help_text=_("Name of the folder in Italian, e.g., 'Documentazione'."), 
        verbose_name=_("Name (IT)")
    )
    description_en = models.TextField(
        help_text=_("Detailed description of the folder in English."), 
        verbose_name=_("Description (EN)"),
        blank=True, 
        null=True
    )
    description_it = models.TextField(
        help_text=_("Detailed description of the folder in Italian."), 
        verbose_name=_("Description (IT)"),
        blank=True, 
        null=True
    )

    def __str__(self):
        return f"{self.project.title_en} - {self.name_en}"

    class Meta:
        verbose_name = _("Folder")
        verbose_name_plural = _("Folders")


class File(models.Model):
    """
    Model representing a file within a folder. Each file has a name, file content,
    and an option to be marked as private.
    """
    folder = models.ForeignKey(
        Folder, 
        related_name='files', 
        on_delete=models.CASCADE, 
        help_text=_("The folder to which this file belongs."), 
        verbose_name=_("Folder")
    )
    name_en = models.CharField(
        max_length=100, 
        help_text=_("Name of the file in English, e.g., 'Project_Plan.pdf'."), 
        verbose_name=_("Name (EN)")
    )
    name_it = models.CharField(
        max_length=100, 
        help_text=_("Name of the file in Italian, e.g., 'Piano_Progetto.pdf'."), 
        verbose_name=_("Name (IT)")
    )
    file = models.FileField(
        upload_to='project_files/', 
        help_text=_("File to be uploaded for the project."), 
        verbose_name=_("File")
    )
    is_private = models.BooleanField(
        default=False, 
        help_text=_("Flag to indicate if the file is private."), 
        verbose_name=_("Is Private")
    )

    def __str__(self):
        return f"{self.folder.name_en} - {self.name_en}"

    class Meta:
        verbose_name = _("File")
        verbose_name_plural = _("Files")


class ContactInfo(models.Model):
    """Model to store site-wide contact information."""
    email = models.EmailField(
        help_text=_("Email address for contacting the site owner."), 
        verbose_name=_("Email")
    )
    linkedin_url = models.URLField(
        max_length=200, 
        blank=True, 
        null=True, 
        help_text=_("LinkedIn profile URL of the site owner."), 
        verbose_name=_("LinkedIn URL")
    )
    github_url = models.URLField(
        max_length=200, 
        blank=True, 
        null=True, 
        help_text=_("GitHub profile URL of the site owner."), 
        verbose_name=_("GitHub URL")
    )

    def __str__(self):
        """Return the email as the string representation."""
        return self.email

    def save(self, *args, **kwargs):
        """
        Ensure only one instance of ContactInfo exists.
        This prevents the creation of multiple instances in the database.
        """
        if not self.pk and ContactInfo.objects.exists():
            raise ValidationError(_('Only one instance of ContactInfo is allowed.'))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Contact Information')
        verbose_name_plural = _('Contact Information')


class Skill(models.Model):
    """Model to represent a skill that can be linked to certificates and education entries."""
    name_en = models.CharField(
        max_length=100, 
        help_text=_("The name of the skill in English (e.g., Python, Data Analysis)."), 
        verbose_name=_("Name (EN)")
    )
    name_it = models.CharField(
        max_length=100, 
        help_text=_("The name of the skill in Italian (e.g., Python, Analisi dei dati)."), 
        verbose_name=_("Name (IT)")
    )

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")


class Certificate(models.Model):
    """Model to store certificates with links to descriptions and course information."""
    title_en = models.CharField(
        max_length=255, 
        help_text=_("The title of the certificate in English."), 
        verbose_name=_("Title (EN)")
    )
    title_it = models.CharField(
        max_length=255, 
        help_text=_("The title of the certificate in Italian."), 
        verbose_name=_("Title (IT)")
    )
    description_en = models.TextField(
        help_text=_("Description of the course in English."), 
        verbose_name=_("Description (EN)")
    )
    description_it = models.TextField(
        help_text=_("Description of the course in Italian."), 
        verbose_name=_("Description (IT)")
    )
    field_en = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text=_("Field of the certificate in English."), 
        verbose_name=_("Field (EN)")
    )
    field_it = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text=_("Field of the certificate in Italian."), 
        verbose_name=_("Field (IT)")
    )
    image = models.ImageField(
        upload_to='certificate_images/', 
        blank=True, 
        null=True, 
        help_text=_("Upload an image for the certificate."), 
        verbose_name=_("Image")
    )
    link = models.URLField(
        help_text=_("URL to the certificate or course information."), 
        verbose_name=_("Link")
    )
    skills = models.ManyToManyField(
        Skill, 
        related_name="certificates", 
        blank=True, 
        help_text=_("Skills related to this certificate."), 
        verbose_name=_("Skills")
    )

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")

class Education(models.Model):
    """Model to store educational background information, such as university and master’s degrees."""
    DEGREE_CHOICES = [
        ('Bachelors', _('Bachelors')),
        ('Masters', _('Masters')),
        ('PhD', _('PhD')),
        ('Other', _('Other')),
    ]

    institution_en = models.CharField(
        max_length=255, 
        help_text=_("Name of the educational institution in English."), 
        verbose_name=_("Institution (EN)")
    )
    institution_it = models.CharField(
        max_length=255, 
        help_text=_("Name of the educational institution in Italian."), 
        verbose_name=_("Institution (IT)")
    )
    degree = models.CharField(
        max_length=50, 
        choices=DEGREE_CHOICES, 
        help_text=_("Degree type (e.g., Bachelor's, Master's)."), 
        verbose_name=_("Degree")
    )
    field_of_study_en = models.CharField(
        max_length=255, 
        help_text=_("Field of study in English (e.g., Computer Science)."), 
        verbose_name=_("Field of Study (EN)")
    )
    field_of_study_it = models.CharField(
        max_length=255, 
        help_text=_("Field of study in Italian (e.g., Informatica)."), 
        verbose_name=_("Field of Study (IT)")
    )
    start_date = models.DateField(
        help_text=_("Start date of the program."), 
        verbose_name=_("Start Date")
    )
    end_date = models.DateField(
        help_text=_("End date of the program, or expected end date."), 
        verbose_name=_("End Date")
    )
    description_en = models.TextField(
        blank=True, 
        help_text=_("Optional description of the program or notable achievements in English."), 
        verbose_name=_("Description (EN)")
    )
    description_it = models.TextField(
        blank=True, 
        help_text=_("Optional description of the program or notable achievements in Italian."), 
        verbose_name=_("Description (IT)")
    )
    skills = models.ManyToManyField(
        'Skill', 
        related_name="educations", 
        blank=True, 
        help_text=_("Skills related to this educational entry."), 
        verbose_name=_("Skills")
    )

    def __str__(self):
        return f"{self.degree} in {self.field_of_study_en} from {self.institution_en}"

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Education")


class Review(models.Model):
    """Model for storing user reviews associated with a project. Reviews are created by users and are subject to admin approval."""
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('approved', _('Approved')),
        ('rejected', _('Rejected')),
    ]

    project = models.ForeignKey(
        'Project', 
        related_name='reviews', 
        on_delete=models.CASCADE, 
        help_text=_("The project this review is associated with."),  
        verbose_name=_("Project")
    )
    reviewer_name = models.CharField(
        max_length=100, 
        help_text=_("Name of the reviewer submitting the review."), 
        verbose_name=_("Reviewer Name")
    )
    content = models.TextField(
        help_text=_("Content of the review."), 
        verbose_name=_("Content")
    )
    
    recommendation = models.BooleanField(
        default=False, 
        help_text=_("Does the reviewer recommend this project?"), 
        verbose_name=_("Recommendation")
    )
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='pending', 
        help_text=_("Approval status of the review."), 
        verbose_name=_("Status")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text=_("Timestamp for when the review was created."), 
        verbose_name=_("Created At")
    )

    def __str__(self):
        return f"Review by {self.reviewer_name} on {self.project.title_en}"

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")


class JobExperience(models.Model):
    """Model to represent a job experience entry associated with various skills."""
    title_en = models.CharField(
        max_length=255, 
        help_text=_("Job title in English (e.g., Software Developer)"), 
        verbose_name=_("Title (EN)")
    )
    title_it = models.CharField(
        max_length=255, 
        help_text=_("Job title in Italian (e.g., Sviluppatore Software)"), 
        verbose_name=_("Title (IT)")
    )
    company = models.CharField(
        max_length=255, 
        help_text=_("Company name"), 
        verbose_name=_("Company")
    )
    start_date = models.DateField(
        help_text=_("Start date of the job"), 
        verbose_name=_("Start Date")
    )
    end_date = models.DateField(
        null=True, 
        blank=True, 
        help_text=_("End date of the job (if applicable)"), 
        verbose_name=_("End Date")
    )
    description_en = models.TextField(
        blank=True, 
        help_text=_("Description of responsibilities or achievements in English"), 
        verbose_name=_("Description (EN)")
    )
    description_it = models.TextField(
        blank=True, 
        help_text=_("Description of responsibilities or achievements in Italian"), 
        verbose_name=_("Description (IT)")
    )
    skills = models.ManyToManyField(
        'Skill', 
        related_name="job_experiences", 
        blank=True, 
        help_text=_("Skills related to this job experience"), 
        verbose_name=_("Skills")
    )

    def __str__(self):
        return f"{self.title_en} at {self.company}"

    class Meta:
        verbose_name = _("Job Experience")
        verbose_name_plural = _("Job Experiences")

class Section(models.Model):
    """Model to represent personal description."""
    title_en = models.CharField(
        max_length=200,
        help_text=_("Title of the section in English"),
        verbose_name=_("Title (EN)")
    )
    title_it = models.CharField(
        max_length=200,
        help_text=_("Title of the section in Italian"),
        verbose_name=_("Title (IT)")
    )
    description_en = models.TextField(
        help_text=_("Description content for the section in English"),
        verbose_name=_("Description (EN)")
    )
    description_it = models.TextField(
        help_text=_("Description content for the section in Italian"),
        verbose_name=_("Description (IT)")
    )

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")


class Category(models.Model):
    """Model representing a blog category."""
    name_en = models.CharField(
        max_length=100, 
        help_text=_("Name of the category in English."), 
        verbose_name=_("Name (EN)")
    )
    name_it = models.CharField(
        max_length=100, 
        help_text=_("Name of the category in Italian."), 
        verbose_name=_("Name (IT)")
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True,
        help_text=_("URL-friendly identifier for the category (auto-generated)."),
        verbose_name=_("Slug")
    )

    def save(self, *args, **kwargs):
        """
        Automatically generate a slug from the category name if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.name_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class BlogPost(models.Model):
    """Model representing a blog post."""
    title_en = models.CharField(
        max_length=200, 
        help_text=_("Title of the blog post in English."), 
        verbose_name=_("Title (EN)")
    )
    title_it = models.CharField(
        max_length=200, 
        help_text=_("Title of the blog post in Italian."), 
        verbose_name=_("Title (IT)")
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        help_text=_("URL-friendly identifier for the post (auto-generated)."),
        verbose_name=_("Slug")
    )
    content_en = models.TextField(
        help_text=_("Main content of the blog post in English."), 
        verbose_name=_("Content (EN)")
    )
    content_it = models.TextField(
        help_text=_("Main content of the blog post in Italian."), 
        verbose_name=_("Content (IT)")
    )
    excerpt_en = models.TextField(
        blank=True, 
        help_text=_("Short summary or excerpt of the blog post in English."), 
        verbose_name=_("Excerpt (EN)")
    )
    excerpt_it = models.TextField(
        blank=True, 
        help_text=_("Short summary or excerpt of the blog post in Italian."), 
        verbose_name=_("Excerpt (IT)")
    )
    featured_image = models.ImageField(
        upload_to='blog_images/',
        blank=True,
        null=True,
        help_text=_("Optional featured image for the blog post."),
        verbose_name=_("Featured Image")
    )
    publication_date = models.DateField(
        auto_now_add=True, 
        help_text=_("Date the blog post was published."), 
        verbose_name=_("Publication Date")
    )
    categories = models.ManyToManyField(
        Category,
        related_name='blog_posts',
        help_text=_("Categories associated with the blog post."),
        verbose_name=_("Categories")
    )
    author = models.CharField(
        max_length=100, 
        help_text=_("Author of the blog post."), 
        verbose_name=_("Author")
    )

    def save(self, *args, **kwargs):
        """
        Automatically generate a slug from the blog post title if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en

    class Meta:
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")
