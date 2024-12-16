from django.contrib import admin
from .models import (
    Project, Folder, File, ContactInfo, Certificate, Education,
    Review, Skill, JobExperience, Section, Category, BlogPost
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Custom admin class for the Project model.
    """
    list_display = ('title_en', 'title_it', 'date', 'is_public')
    search_fields = ('title_en', 'title_it', 'description_en', 'description_it')
    list_filter = ('is_public', 'date')
    ordering = ('-date',)

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_it', 'project')
    search_fields = ('name_en', 'name_it')
    list_filter = ('project',)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_it', 'folder', 'is_private')
    search_fields = ('name_en', 'name_it')
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
    list_display = ('name_en', 'name_it', 'related_certificates', 'related_educations', 'related_job_experiences')
    search_fields = ('name_en', 'name_it')
    inlines = [CertificateInline, EducationInline, JobExperienceInline]

    def related_certificates(self, obj):
        return ", ".join([certificate.title_en for certificate in obj.certificates.all()])
    related_certificates.short_description = "Certificates"

    def related_educations(self, obj):
        return ", ".join([f"{education.degree} in {education.field_of_study_en}" for education in obj.educations.all()])
    related_educations.short_description = "Education Entries"

    def related_job_experiences(self, obj):
        return ", ".join([job.title_en for job in obj.job_experiences.all()])
    related_job_experiences.short_description = "Job Experiences"


@admin.register(JobExperience)
class JobExperienceAdmin(admin.ModelAdmin):
    """Admin class for managing JobExperience model."""
    list_display = ('title_en', 'title_it', 'company', 'start_date', 'end_date')
    search_fields = ('title_en', 'title_it', 'company', 'description_en', 'description_it')
    list_filter = ('start_date', 'end_date')
    filter_horizontal = ('skills',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_it', 'link')
    search_fields = ('title_en', 'title_it')
    filter_horizontal = ('skills',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution_en', 'institution_it', 'degree', 'field_of_study_en', 'start_date', 'end_date')
    search_fields = ('institution_en', 'institution_it', 'degree', 'field_of_study_en', 'field_of_study_it')
    filter_horizontal = ('skills',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin interface for managing user reviews."""
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
    list_display = ('title_en', 'title_it', 'description_en', 'description_it')
    search_fields = ('title_en', 'title_it', 'description_en', 'description_it')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model in blogs."""
    list_display = ('name_en', 'name_it', 'slug')
    prepopulated_fields = {'slug': ('name_en',)}
    search_fields = ('name_en', 'name_it')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Admin configuration for BlogPost model."""
    list_display = ('title_en', 'title_it', 'author', 'publication_date')
    list_filter = ('categories', 'publication_date')
    search_fields = ('title_en', 'title_it', 'content_en', 'content_it')
    prepopulated_fields = {'slug': ('title_en',)}
    date_hierarchy = 'publication_date'
    filter_horizontal = ('categories',)
