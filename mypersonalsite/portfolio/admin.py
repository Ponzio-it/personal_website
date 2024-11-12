from django.contrib import admin
from .models import Project, Folder, File, ContactInfo, Certificate, Education

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
    list_display = ('email', 'linkedin_url', 'github_url')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'field_of_study', 'start_date', 'end_date')