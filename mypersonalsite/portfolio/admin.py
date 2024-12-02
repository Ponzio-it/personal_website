from django.contrib import admin
from .models import (
    Project, Folder, File, ContactInfo, Certificate, Education,
    Review, Skill, JobExperience, Section, Category, BlogPost
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_public')
    search_fields = ('title', 'description')
    list_filter = ('is_public', 'date')
    ordering = ('-date',)


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    search_fields = ('name',)
    list_filter = ('project',)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'folder', 'is_private')
    search_fields = ('name',)
    list_filter = ('is_private', 'folder')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """Admin view for managing ContactInfo model."""
    list_display = ('email', 'linkedin_url', 'github_url')
    list_editable = ('linkedin_url', 'github_url')


# Inline relationships for Skill model
class CertificateInline(admin.TabularInline):
    model = Certificate.skills.through
    extra = 1


class EducationInline(admin.TabularInline):
    model = Education.skills.through
    extra = 1


class JobExperienceInline(admin.TabularInline):
    model = JobExperience.skills.through
    extra = 1


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """
    Custom admin class for Skill model. 
    Displays related certificates, educations, and job experiences.
    """
    list_display = ('name', 'related_certificates', 'related_educations', 'related_job_experiences')
    search_fields = ('name',)
    inlines = [CertificateInline, EducationInline, JobExperienceInline]

    def related_certificates(self, obj):
        return ", ".join([certificate.title for certificate in obj.certificates.all()])
    related_certificates.short_description = "Certificates"

    def related_educations(self, obj):
        return ", ".join([f"{education.degree} in {education.field_of_study}" for education in obj.educations.all()])
    related_educations.short_description = "Education Entries"

    def related_job_experiences(self, obj):
        return ", ".join([job.title for job in obj.job_experiences.all()])
    related_job_experiences.short_description = "Job Experiences"


@admin.register(JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    """
    Admin class for managing JobExperience model.
    """
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company', 'description')
    list_filter = ('start_date', 'end_date')
    filter_horizontal = ('skills',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title',)
    filter_horizontal = ('skills',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'field_of_study', 'start_date', 'end_date')
    search_fields = ('institution', 'degree', 'field_of_study')
    filter_horizontal = ('skills',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin interface for managing user reviews.
    Allows bulk approval or rejection.
    """
    list_display = ('reviewer_name', 'project', 'recommendation', 'status', 'created_at')
    list_filter = ('status', 'recommendation')
    actions = ['approve_reviews', 'reject_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(status='approved')
    approve_reviews.short_description = "Approve selected reviews"

    def reject_reviews(self, request, queryset):
        queryset.update(status='rejected')
    reject_reviews.short_description = "Reject selected reviews"


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    """Admin interface for managing personal description sections."""
    list_display = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for Category model in blogs.
    """
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Admin configuration for BlogPost model.
    """
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('categories', 'publication_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publication_date'
    filter_horizontal = ('categories',)
