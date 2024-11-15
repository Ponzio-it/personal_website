# portfolio/views.py

import os
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from django.http import FileResponse, Http404
from .models import Project, ContactInfo, Certificate, Education, Review, Skill, JobExperience
from .form  import ReviewForm

# Home page view
def home(request):
    """Render the home page."""
    return render(request, 'portfolio/home.html')

def education(request):
    """
    Render the Education page, displaying a list of skills, certificates,
    and educational history, and job experiences. Filter entries by selected skill if provided.
    """
    # Fetch all skills
    skills = Skill.objects.all()

    # Filter certificates and education by selected skill if provided
    skill_id = request.GET.get('skill')
    if skill_id:
        selected_skill = get_object_or_404(Skill, id=skill_id)
        certificates = Certificate.objects.filter(skills__id=skill_id)
        education_history = Education.objects.filter(skills__id=skill_id)
        job_experiences = JobExperience.objects.filter(skills=selected_skill).order_by('-end_date')
    else:
        selected_skill = None
        certificates = Certificate.objects.all()
        education_history = Education.objects.order_by('-end_date')  # Order by most recent first
        job_experiences = JobExperience.objects.order_by('-end_date')

    context = {
        'skills': skills,
        'certificates': certificates,
        'education_history': education_history,
        'job_experiences': job_experiences,
        'selected_skill': selected_skill,
    }
    return render(request, 'portfolio/education.html', context)
    

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

def contact(request):
    """
    Render the Contact page, displaying site-wide contact information
    like email, LinkedIn, and GitHub links.
    """
    contact_info = ContactInfo.objects.first()  # Retrieve the single ContactInfo instance
    context = {
        'contact_info': contact_info
    }
    return render(request, 'portfolio/contact.html', context)

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


class ProjectDetailView(DetailView):
    """
    View for displaying details of a single project, along with approved reviews.
    """
    model = Project
    template_name = 'portfolio/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include only approved reviews in the context
        context['reviews'] = self.object.reviews.filter(status='approved')
        return context


class ReviewCreateView(CreateView):
    """
    View for handling the submission of a new review for a project.
    The review status is set to 'pending' and awaits admin approval.
    """
    model = Review
    form_class = ReviewForm
    template_name = 'portfolio/review_form.html'

    def form_valid(self, form):
        # Set the project for the review and mark the status as 'pending'
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.status = 'pending'
        form.save()
        return redirect(reverse('portfolio:project_detail', args=[self.kwargs['pk']]))
    
    def get_context_data(self, **kwargs):
        # Pass the project to the template context
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return context
    
def redirect_to_linkedin(request):
    """Redirects to the LinkedIn profile."""
    return redirect("https://www.linkedin.com/in/ettore-ponzio")

def redirect_to_github(request):
    """Redirects to the GitHub profile."""
    return redirect("https://github.com/Ponzio-it")