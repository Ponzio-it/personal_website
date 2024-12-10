from django.urls import path
from . import views
from .views import (
    ProjectDetailView,
    ReviewCreateView,
    ViewEducationDetail,
    ViewJobExperienceDetail,
    ViewCertificateDetail,
    ViewJobExperienceList,
    ViewEducationList,
    ViewCertificateList,
)

app_name = 'portfolio'

# URL patterns for the portfolio app
urlpatterns = [
    # Home and static pages
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('open-cv/', views.open_cv, name='open_cv'),  # URL for downloading the CV

    # Project-related URLs
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/review/', ReviewCreateView.as_view(), name='project_review'),

    # External redirects
    path('linkedin/', views.redirect_to_linkedin, name='linkedin'),
    path('github/', views.redirect_to_github, name='github'),

    # Folder and file details
    path('folders/<int:pk>/', views.FolderDetailView.as_view(), name='folder_detail'),

    # Blog-related URLs
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),

    # Education, Certificate, and Job Experience list
    path('job-experiences/', ViewJobExperienceList.as_view(), name='job_experience_list'),
    path('education-background/', ViewEducationList.as_view(), name='education_list'),
    path('certificates/', ViewCertificateList.as_view(), name='certificate_list'),
    
    # Education, Certificate, and Job Experience details
    path('education/<int:pk>/', ViewEducationDetail.as_view(), name='education_detail'),
    path('job_experience/<int:pk>/', ViewJobExperienceDetail.as_view(), name='job_experience_detail'),
    path('certificate/<int:pk>/', ViewCertificateDetail.as_view(), name='certificate_detail'),
]
