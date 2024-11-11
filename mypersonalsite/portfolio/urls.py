# portfolio/urls.py

from django.urls import path
from . import views

app_name = 'portfolio' 

# URL patterns for the portfolio app
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_me, name='about_me'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    # URL for downloading the CV
    path('open-cv/', views.open_cv, name='open_cv'),
]
