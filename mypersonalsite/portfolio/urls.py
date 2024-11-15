# portfolio/urls.py

from django.urls import path
from . import views
from .views import ProjectDetailView, ReviewCreateView

app_name = 'portfolio' 

# URL patterns for the portfolio app
urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    # URL for downloading the CV
    path('open-cv/', views.open_cv, name='open_cv'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/review/', ReviewCreateView.as_view(), name='project_review'),
    path('linkedin/', views.redirect_to_linkedin, name='linkedin'),
    path('github/', views.redirect_to_github, name='github'),
]
