import os
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from django.http import FileResponse, Http404
from .models import Project, ContactInfo, Certificate, Education, Review, Skill, JobExperience, Section, Folder, BlogPost, Category
from .form  import ReviewForm, ContactForm
from django.core.mail import send_mail
from django.db.models import Q
from django.utils.translation import gettext as _ 
from django.contrib import messages

# Home page view
def home(request):
    """Render the home page with dynamic sections."""
    sections = Section.objects.all()
    return render(request, 'portfolio/home.html', {'sections': sections})

def education(request):
    """
    Render the Education page, displaying a list of skills, certificates,
    and educational history, and job experiences. Filter entries by selected skill if provided.
    """
    # Fetch all skills
    skills = Skill.objects.all()

    # Filter certificates and education by selected skill if provided
    skill_ids = request.GET.getlist('skill')
    selected_skills = Skill.objects.filter(id__in=skill_ids) if skill_ids else []

    if skill_ids:        
        certificates = Certificate.objects.filter(skills__id__in=skill_ids).only('title','field').distinct()
        education_history = Education.objects.filter(skills__id__in=skill_ids).only('institution', 'degree', 'field_of_study', 'start_date', 'end_date').distinct()
        job_experiences = JobExperience.objects.filter(skills__id__in=skill_ids).only('title', 'company', 'start_date', 'end_date').order_by('-end_date').distinct()
    else:        
        certificates = Certificate.objects.only('title','field').all()
        education_history = Education.objects.only('institution', 'degree', 'field_of_study', 'start_date', 'end_date').order_by('-end_date')
        job_experiences = JobExperience.objects.only('title', 'company', 'start_date', 'end_date').order_by('-end_date')

    
    context = {
        'skills': skills,
        'selected_skill': selected_skills,
        'certificates': certificates,
        'education_history': education_history,
        'job_experiences': job_experiences,
        
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
    Render the contact page with a form for user messages.
    Handles form submissions to send emails to the site owner.
    """
    # Retrieve the contact information (email address) from the database
    contact_info = ContactInfo.objects.first()

    # Instantiate the form
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        # Validate the form
        if form.is_valid():
            # Extract cleaned data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Compose the email message
            full_message = _(
                "Message from {first_name} {last_name} ({email}):\n\n{message}"
            ).format(
                first_name=first_name,
                last_name=last_name,
                email=email,
                message=message,
            )

            # Send the email to the site owner's email address
            send_mail(
                subject=_("Contact Form Submission"),
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact_info.email],
                fail_silently=False,
            )

            # Render the template with a success message
            return render(
                request,
                'portfolio/contact.html',
                {
                    'form': ContactForm(),  # Empty form for new submissions
                    'contact_info': contact_info,
                    'success': True,  # Success flag for user feedback
                },
            )

    # Render the contact page with the form
    return render(
        request,
        'portfolio/contact.html',
        {'form': form, 'contact_info': contact_info},
    )

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
        raise Http404(_("The requested CV could not be found."))

class ProjectDetailView(DetailView):
    """
    View for displaying details of a single project, along with approved reviews.
    """
    model = Project
    template_name = 'portfolio/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include only approved reviews in the context
        # Prefetch related folders and files
        context['folders'] = self.object.folders.prefetch_related('files').all()
        context['reviews'] = self.object.reviews.filter(status='approved')
        return context

class FolderDetailView(DetailView):
    """
    View for displaying details of a single folder, including its files.
    """
    model = Folder
    template_name = 'portfolio/folder_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add files related to the folder to the context
        context['files'] = self.object.files.all()
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

        # Send email notification to admin
        send_mail(
            subject=_('New Review Submission Pending Approval'),
            message=_(f"A new review has been submitted for the project: {form.instance.project.title}. Please review and approve it."),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        # Add a popup message for the user
        messages.info(self.request, _("Your review has been submitted and is pending approval. Thank you!"))

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

def blog_list(request):
    """
    View to display the list of blog posts.
    """
    query = request.GET.get('q')  # Capture the search query from the URL
    posts = BlogPost.objects.all().order_by('-publication_date')
    categories = Category.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    context = {
        'posts': posts,
        'categories': categories,
        'query': query,
    }

    return render(request, 'portfolio/blog_list.html', context)

def blog_detail(request, slug):
    """
    View to display the details of a single blog post.
    """
    post = get_object_or_404(BlogPost, slug=slug)
    related_posts = BlogPost.objects.filter(
        categories__in=post.categories.all()
    ).exclude(id=post.id)[:3]

    context = {
        'post': post,
        'related_posts': related_posts,
    }

    return render(request, 'portfolio/blog_detail.html', context)

class ViewEducationDetail(DetailView):
    """
    View for rendering detailed information about a specific education entry.
    """
    model = Education
    template_name = 'portfolio/education_detail.html'
    context_object_name = 'education'

class ViewJobExperienceDetail(DetailView):
    """
    View for rendering detailed information about a specific job experience entry.
    """
    model = JobExperience
    template_name = 'portfolio/job_experience_detail.html'
    context_object_name = 'job_experience'

class ViewCertificateDetail(DetailView):
    """
    View for rendering detailed information about a specific certificate entry.
    """
    model = Certificate
    template_name = 'portfolio/certificate_detail.html'
    context_object_name = 'certificate'

def folders_view(request):
    """
    View to render the folders list with file counts.
    """
    folders = Folder.objects.prefetch_related('files')  # Prefetch related files
    context = {
        'folders': folders,
    }
    return render(request, 'portfolio/project_detail.html', context)