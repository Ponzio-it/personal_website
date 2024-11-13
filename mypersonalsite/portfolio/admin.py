from django.contrib import admin
from .models import Project, Folder, File, ContactInfo, Certificate, Education, Review

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