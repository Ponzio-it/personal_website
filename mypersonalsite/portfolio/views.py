# portfolio/views.py

import os
from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse, Http404
from .models import Project

# Home page view
def home(request):
    """Render the home page."""
    return render(request, 'portfolio/home.html')

# About Me page view
def about_me(request):
    """Render the About Me page."""
    return render(request, 'portfolio/about_me.html')

# Projects page view with dynamic data
def projects(request):
    """
    Render the Projects page, displaying all projects along with their related
    folders and files.
    """
    # Query all projects, including their related folders and files
    projects = Project.objects.prefetch_related('folders__files').filter(is_public=True)

    context = {
        'projects': projects
    }
    return render(request, 'portfolio/projects.html', context)

# Contact page view
def contact(request):
    """Render the Contact page."""
    return render(request, 'portfolio/contact.html')

# Open CV page view
def open_cv(request):
    """Handle the download of the CV (PDF file)."""
    # Construct the full path to the PDF file in the static directory
    file_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'portfolio', 'docs', 'CV_Ettore Ponzio_eng.pdf')

    # Try to open the file and return it as a FileResponse
    try:
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        # If the file is not found, raise a 404 error
        raise Http404("The requested CV could not be found.")

