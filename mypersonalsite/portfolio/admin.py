from django.contrib import admin
from .models import Project, Folder, File, ContactInfo, Certificate, Education, Review, Skill, JobExperience, Section, Category, BlogPost

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_public')  # Display these fields in the admin list view
    search_fields = ('title', 'description')  # Searchable fields
    list_filter = ('is_public', 'date')  # Filters for quick access
    ordering = ('-date',)  # Default ordering by date, newest first

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')  # Display folder name and related project
    search_fields = ('name',)
    list_filter = ('project',)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'folder', 'is_private')  # Display file name, folder, and privacy status
    search_fields = ('name',)
    list_filter = ('is_private', 'folder')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """Admin view for managing ContactInfo model."""

    # Define fields to display in the admin list view
    list_display = ('email','linkedin_url', 'github_url')
    list_editable = ('linkedin_url', 'github_url')


#make possible add relationship to certificate, education and job experience when add Skills in admin

class CertificateInline(admin.TabularInline):  # Use StackedInline for more detailed forms
    model = Certificate.skills.through  # Access the ManyToMany relationship table
    extra = 1  # Number of empty forms to display

class EducationInline(admin.TabularInline):
    model = Education.skills.through
    extra = 1

class JobExperienceInline(admin.TabularInline):
    model = JobExperience.skills.through
    extra = 1

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    '''
    Custom admin class for the Skill model. This class allows managing
    skills and displays related certificates and education entries
    directly in the admin list view for easy access.'''

    list_display = ('name', 'related_certificates', 'related_educations','related_job_experiences')
    search_fields = ('name',)
    inlines = [CertificateInline, EducationInline, JobExperienceInline]


    def related_certificates(self, obj):
        return ", ".join([certificate.title for certificate in obj.certificates.all()])
    related_certificates.short_description = "Certificates"

    def related_educations(self, obj):
        return ", ".join([education.degree + " in " + education.field_of_study for education in obj.educations.all()])
    related_educations.short_description = "Education Entries"


    def related_job_experiences(self, obj):
        return ", ".join([job.title for job in obj.job_experiences.all()])
    related_job_experiences.short_description = "Job Experiences"

@admin.register(JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    """
    Admin class for the JobExperience model.
    Displays detailed information about job experiences.
    """
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company', 'description')
    list_filter = ('start_date', 'end_date')
    filter_horizontal = ('skills',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)
    filter_horizontal = ('skills',)  # This enables a horizontal filter for selecting skills



@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'field_of_study', 'start_date', 'end_date')
    search_fields = ('institution', 'degree', 'field_of_study')
    filter_horizontal = ('skills',)  # This enables a horizontal filter for selecting skills


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin interface for managing user reviews on projects.
    Allows admins to approve or reject reviews submitted by users.
    """
    
    list_display = ('reviewer_name', 'project', 'recommendation', 'status', 'created_at')
    # Display reviewer name, project, recommendation, status, and created date in the list view

    list_filter = ('status', 'recommendation')  # Filter by review status and recommendation

    actions = ['approve_reviews', 'reject_reviews']  # Add bulk action buttons for review approval/rejection

    def approve_reviews(self, request, queryset):
        """
        Custom admin action to mark selected reviews as 'approved'.
        """
        queryset.update(status='approved')
    approve_reviews.short_description = "Approve selected reviews"

    def reject_reviews(self, request, queryset):
        """
        Custom admin action to mark selected reviews as 'rejected'.
        """
        queryset.update(status='rejected')
    reject_reviews.short_description = "Reject selected reviews"


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """"Admin interface to add personal description"""
    list_display = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for Category model.
    """
    list_display = ('name', 'slug')  # Display name and slug in the admin list
    prepopulated_fields = {'slug': ('name',)}  # Auto-fill slug based on name
    search_fields = ('name',)  # Add a search bar for categories


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for BlogPost model.
    """
    list_display = ('title', 'author', 'publication_date')  # Columns to display in the admin list
    list_filter = ('categories', 'publication_date')  # Add filters for categories and publication date
    search_fields = ('title', 'content')  # Add a search bar for posts
    prepopulated_fields = {'slug': ('title',)}  # Auto-fill slug based on title
    date_hierarchy = 'publication_date'  # Add a date hierarchy filter
    filter_horizontal = ('categories',)  # Display categories as a horizontal filter for many-to-many field