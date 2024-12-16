import os
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.views.generic import DetailView, CreateView, ListView
from django.http import FileResponse, Http404
from django.core.mail import send_mail
from django.db.models import Q
from django.utils.translation import gettext as _
from django.contrib import messages
from django.templatetags.static import static
from django.utils.translation import get_language



from .models import (
    Project,
    ContactInfo,
    Certificate,
    Education,
    Review,
    Skill,
    JobExperience,
    Section,
    Folder,
    BlogPost,
    Category,
)
from .form import ReviewForm, ContactForm


# Home page view
def home(request):
    """
    Render the home page with dynamic bilingual sections.
    """
    user_language = get_language()  # Get the current user's language (e.g., 'en' or 'it')
    sections = Section.objects.all()
    
    # Dynamically set display fields for bilingual support
    for section in sections:
        if user_language == 'it':
            section.display_title = section.title_it
            section.display_description = section.description_it
        else:
            section.display_title = section.title_en
            section.display_description = section.description_en

    context = {'sections': sections}
    return render(request, 'portfolio/home.html', context)


def education(request):
    """ 
    Render the Education page, displaying a list of skills, certificates, 
    educational history, and job experiences. Filter entries by selected skill if provided. 
    """
    user_language = get_language()  # Get the current language, e.g., 'en' or 'it'
    skills = Skill.objects.all()
    
    # Filter by selected skill(s) if any are selected
    skill_ids = request.GET.getlist('skill')
    selected_skills = Skill.objects.filter(id__in=skill_ids) if skill_ids else []
    
    if skill_ids:
        certificates = Certificate.objects.filter(skills__id__in=skill_ids).distinct()
        education_history = Education.objects.filter(skills__id__in=skill_ids).distinct()
        job_experiences = JobExperience.objects.filter(skills__id__in=skill_ids).order_by('-end_date').distinct()
    else:
        certificates = Certificate.objects.all()
        education_history = Education.objects.all().order_by('-end_date')
        job_experiences = JobExperience.objects.all().order_by('-end_date')

    # Dynamically set the bilingual fields based on the user's language
    for education in education_history:
        if user_language == 'it':
            education.display_institution = education.institution_it
            education.display_field_of_study = education.field_of_study_it
        else:
            education.display_institution = education.institution_en
            education.display_field_of_study = education.field_of_study_en

    for job in job_experiences:
        if user_language == 'it':
            job.display_title = job.title_it
        else:
            job.display_title = job.title_en

    for skill in skills:
        if user_language == 'it':
            skill.display_name = skill.name_it
        else:
            skill.display_name = skill.name_en

    for certificate in certificates:
        if user_language == 'it':
            certificate.display_title = certificate.title_it
            certificate.display_description = certificate.description_it
        else:
            certificate.display_title = certificate.title_en
            certificate.display_description = certificate.description_en

    context = {
        'skills': skills,
        'selected_skills': selected_skills,
        'certificates': certificates,
        'education_history': education_history,
        'job_experiences': job_experiences,
    }
    return render(request, 'portfolio/education.html', context)



def projects(request):
    """
    Render the Projects page, displaying all projects along with their related
    folders and files.
    """
    user_language = get_language()  # Detect the current language (e.g., 'en' or 'it')

    # Query all projects, including their related folders and files
    projects = Project.objects.prefetch_related('folders__files').filter(is_public=True)

    # Dynamically set the title and description based on the user's language
    for project in projects:
        if user_language == 'it':
            project.display_title = project.title_it
            project.display_description = project.description_it
        else:
            project.display_title = project.title_en
            project.display_description = project.description_en

    context = {'projects': projects}
    return render(request, 'portfolio/projects.html', context)


def contact(request):
    """ 
    Render the contact page with a form for user messages. 
    Handles form submissions to send emails to the site owner. 
    """
    contact_info = ContactInfo.objects.first()  # Retrieve the contact information from the database
    
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            full_message = _(
                "Message from {first_name} {last_name} ({email}):\n\n{message}"
            ).format(
                first_name=first_name,
                last_name=last_name,
                email=email,
                message=message,
            )
            
            send_mail(
                subject=_("Contact Form Submission"),
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact_info.email],
                fail_silently=False,
            )
            
            return render(
                request,
                'portfolio/contact.html',
                {
                    'form': ContactForm(),  # Reset form for new submission
                    'contact_info': contact_info,
                    'success': True,  # Flag to display success message
                },
            )
    
    return render(
        request, 
        'portfolio/contact.html', 
        {'form': form, 'contact_info': contact_info}
    )

# Open CV page view
def open_cv(request):
    """
    Handle the download of the CV (PDF file).
    """
    # Determine the correct base path
    if settings.DEBUG:
        # In development, use STATICFILES_DIRS
        base_path = settings.STATICFILES_DIRS[0]
    else:
        # In production, use STATIC_ROOT
        base_path = settings.STATIC_ROOT

    # Construct the full file path
    file_path = os.path.join(base_path, 'portfolio', 'docs', 'CV_Ettore Ponzio_eng.pdf')


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

         # Get the user's current language (e.g., 'en' or 'it')
        user_language = get_language()

         # Dynamically set the title and description fields for the current language
        project = context['project']
        project.display_title = project.title_it if user_language == 'it' else project.title_en
        project.display_description = project.description_it if user_language == 'it' else project.description_en
        
         # Update folders to support bilingual names
        folders = self.object.folders.prefetch_related('files').all()
        for folder in folders:
            folder.display_name = folder.name_it if user_language == 'it' else folder.name_en

            # Update files to support bilingual names if they have translations
            for file in folder.files.all():
                file.display_name = file.name_it if hasattr(file, 'name_it') and user_language == 'it' else file.name_en if hasattr(file, 'name_en') else file.name

        # Add folders and reviews to the context
        context['folders'] = folders

        context['reviews'] = self.object.reviews.filter(status='approved')
        return context



class FolderDetailView(DetailView):
    """ 
    View for displaying details of a single folder, including its bilingual name, description, and files. 
    """
    model = Folder
    template_name = 'portfolio/folder_detail.html'
    context_object_name = 'folder'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the user's current language (e.g., 'en' or 'it')
        user_language = get_language()
        
        # Dynamically set the folder's bilingual name and description
        folder = context['folder']
        folder.display_name = (
            folder.name_it if user_language == 'it' else folder.name_en
        )
        folder.display_description = (
            folder.description_it if user_language == 'it' else folder.description_en
        )

        # Update files to support bilingual names
        files = self.object.files.all()
        for file in files:
            file.display_name = file.name_it if user_language == 'it' else file.name_en

        # Add files and folder to the context
        context['files'] = files
        context['folder'] = folder

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
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.status = 'pending'
        form.save()

        send_mail(
            subject=_('New Review Submission Pending Approval'),
            message=_('A new review has been submitted for the project: {project_title}. Please review and approve it.').format(
                project_title=form.instance.project.title_en
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        messages.info(
            self.request, 
            _('Your review has been submitted and is pending approval. Thank you!')
        )

        return redirect(reverse('portfolio:project_detail', args=[self.kwargs['pk']]))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return context



def redirect_to_linkedin(request):
    """
    Redirects to the LinkedIn profile.
    """
    return redirect("https://www.linkedin.com/in/ettore-ponzio")


def redirect_to_github(request):
    """
    Redirects to the GitHub profile.
    """
    return redirect("https://github.com/Ponzio-it")



def blog_list(request):
    """ 
    View to display the list of blog posts with bilingual support. 
    """
    query = request.GET.get('q')  # Capture the search query from the URL
    selected_category = request.GET.get('category')  # Capture the selected category
    user_language = get_language()  # Get the user's language (e.g., 'en' or 'it')

    # Query all blog posts and categories
    posts = BlogPost.objects.all().order_by('-publication_date')
    categories = Category.objects.all()

    # Filter posts by query, checking title and content for the current language
    if query:
        if user_language == 'it':
            posts = posts.filter(
                Q(title_it__icontains=query) | Q(content_it__icontains=query)
            )
        else:
            posts = posts.filter(
                Q(title_en__icontains=query) | Q(content_en__icontains=query)
            )

    # Filter posts by the selected category
    if selected_category:
        posts = posts.filter(categories__slug=selected_category)

    # Dynamically set display fields for bilingual support
    for post in posts:
        if user_language == 'it':
            post.display_title = post.title_it
            post.display_content = post.content_it
            post.display_excerpt = post.excerpt_it  # Ensure you have excerpt_it field
        else:
            post.display_title = post.title_en
            post.display_content = post.content_en
            post.display_excerpt = post.excerpt_en  # Ensure you have excerpt_en field

    # Dynamically set display names for categories based on the user's language
    for category in categories:
        if user_language == 'it':
            category.display_name = category.name_it
        else:
            category.display_name = category.name_en
    context = {
        'posts': posts,
        'categories': categories,
        'query': query,
        'selected_category': selected_category  # Pass to the template to highlight active category
    }
    
    return render(request, 'portfolio/blog_list.html', context)

def blog_detail(request, slug):
    """ 
    View to display the details of a single blog post with bilingual support. 
    """
    user_language = get_language()  # Detect the current language (e.g., 'en' or 'it')
    post = get_object_or_404(BlogPost, slug=slug)
    
    # Dynamically set bilingual fields for the current language
    if user_language == 'it':
        post.display_title = post.title_it
        post.display_content = post.content_it
        post.display_excerpt = post.excerpt_it
    else:
        post.display_title = post.title_en
        post.display_content = post.content_en
        post.display_excerpt = post.excerpt_en
    
    related_posts = BlogPost.objects.filter(
        categories__in=post.categories.all()
    ).exclude(id=post.id)[:3]

    # Dynamically set bilingual fields for related posts
    for related_post in related_posts:
        if user_language == 'it':
            related_post.display_title = related_post.title_it
        else:
            related_post.display_title = related_post.title_en

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

    def get_context_data(self, **kwargs):
        """ Add bilingual context for Education details """
        context = super().get_context_data(**kwargs)
        user_language = get_language()  # Get the current user's language (e.g., 'en' or 'it')

        # Set display fields dynamically based on the current language
        education = context['education']
        context['education'].display_institution = (
            education.institution_it if user_language == 'it' else education.institution_en
        )
        context['education'].display_field_of_study = (
            education.field_of_study_it if user_language == 'it' else education.field_of_study_en
        )
        context['education'].display_description = (
            education.description_it if user_language == 'it' else education.description_en
        )

        return context


class ViewJobExperienceDetail(DetailView):
    """
    View for rendering detailed information about a specific job experience entry.
    """
    model = JobExperience
    template_name = 'portfolio/job_experience_detail.html'
    context_object_name = 'job_experience'

    def get_context_data(self, **kwargs):
        """ Add bilingual context for Job Experience details """
        context = super().get_context_data(**kwargs)
        user_language = get_language()  # Get the current user's language (e.g., 'en' or 'it')

        # Set display fields dynamically based on the current language
        job_experience = context['job_experience']
        context['job_experience'].display_title = (
            job_experience.title_it if user_language == 'it' else job_experience.title_en
        )
        context['job_experience'].display_description = (
            job_experience.description_it if user_language == 'it' else job_experience.description_en
        )

        return context


class ViewCertificateDetail(DetailView):
    """
    View for rendering detailed information about a specific certificate entry.
    """
    model = Certificate
    template_name = 'portfolio/certificate_detail.html'
    context_object_name = 'certificate'

    def get_context_data(self, **kwargs):
        """ Add bilingual context for Certificate details """
        context = super().get_context_data(**kwargs)
        user_language = get_language()  # Get the current user's language (e.g., 'en' or 'it')

        # Set display fields dynamically based on the current language
        certificate = context['certificate']
        context['certificate'].display_title = (
            certificate.title_it if user_language == 'it' else certificate.title_en
        )
        certificate = context['certificate']
        context['certificate'].display_field = (
            certificate.field_it if user_language == 'it' else certificate.field_en
        )
        
        context['certificate'].display_description = (
            certificate.description_it if user_language == 'it' else certificate.description_en
        )
        
        related_skills = certificate.skills.all()
        for skill in related_skills:
            skill.display_name = (
                skill.name_it if user_language == 'it' else skill.name_en
            )

        context['skills'] = related_skills

        return context


def folders_view(request):
    """
    View to render the folders list with file counts.
    """
    # Prefetch related files for efficiency
    folders = Folder.objects.prefetch_related('files')

    context = {
        'folders': folders,
    }
    return render(request, 'portfolio/project_detail.html', context)



class ViewJobExperienceList(ListView):
    """
    View for listing all job experiences with bilingual support.
    """
    model = JobExperience
    template_name = 'portfolio/job_experience_list.html'
    context_object_name = 'job_experiences'

    def get_queryset(self):
        """Retrieve the job experiences and annotate the bilingual fields based on the user's language."""
        user_language = get_language()  # Detect the current language (e.g., 'en' or 'it')
        queryset = JobExperience.objects.all()
        
        # Dynamically set the title and description fields for the language
        for job_experience in queryset:
            if user_language == 'it':
                job_experience.display_title = job_experience.title_it
                job_experience.display_description = job_experience.description_it
            else:
                job_experience.display_title = job_experience.title_en
                job_experience.display_description = job_experience.description_en
        
        return queryset

    def get_context_data(self, **kwargs):
        """Add context data to the template with bilingual support for title and description."""
        context = super().get_context_data(**kwargs)
        
        user_language = get_language()  # Detect the current language (e.g., 'en' or 'it')
        
        # Update display fields in the context based on the current language
        for job_experience in context['job_experiences']:
            if user_language == 'it':
                job_experience.display_title = job_experience.title_it
                job_experience.display_description = job_experience.description_it
            else:
                job_experience.display_title = job_experience.title_en
                job_experience.display_description = job_experience.description_en
        
        return context

class ViewEducationList(ListView):
    """
    View for listing all education entries with bilingual support.
    """
    model = Education
    template_name = 'portfolio/education_list.html'
    context_object_name = 'educations'

    def get_queryset(self):
        """Retrieve the education entries and annotate the bilingual fields based on the user's language."""
        user_language = get_language()  # Detect the current language (e.g., 'en' or 'it')
        queryset = Education.objects.all()
        
        # Dynamically set the title and description fields for the language
        for education in queryset:
            if user_language == 'it':
                education.degree
                education.display_institution = education.institution_it
            else:
                education.degree
                education.display_institution = education.institution_en
        
        return queryset

    def get_context_data(self, **kwargs):
        """Add context data to the template with bilingual support for title and description."""
        context = super().get_context_data(**kwargs)
        
        user_language = get_language()  # Detect the current language (e.g., 'en' or 'it')
        
        # Update display fields in the context based on the current language
        for education in context['educations']:
            if user_language == 'it':
                education.degree
                education.display_description = education.description_it
            else:
                education.degree
                education.display_description = education.description_en
        
        return context
    
class ViewCertificateList(ListView):
    """
    View for listing all certificates with bilingual support.
    """
    model = Certificate
    template_name = 'portfolio/certificate_list.html'
    context_object_name = 'certificates'
    paginate_by = 10

    def get_queryset(self):
        """Retrieve the certificates and annotate the bilingual fields based on the user's language."""
        user_language = get_language()  # Detect the current language (e.g., 'en' or 'it')
        queryset = Certificate.objects.all()
        
        # Dynamically set the title and description fields for the language
        for certificate in queryset:
            if user_language == 'it':
                certificate.display_title = certificate.title_it
                certificate.display_field = certificate.field_it
                certificate.display_description = certificate.description_it
            else:
                certificate.display_title = certificate.title_en
                certificate.display_field = certificate.field_en
                certificate.display_description = certificate.description_en
        
        return queryset

    def get_context_data(self, **kwargs):
        """Add context data to the template with bilingual support for title and description."""
        context = super().get_context_data(**kwargs)
        
        user_language = get_language()  # Detect the current language (e.g., 'en' or 'it')
        
        # Update display fields in the context based on the current language
        for certificate in context['certificates']:
            if user_language == 'it':
                certificate.display_title = certificate.title_it
                certificate.display_description = certificate.description_it
            else:
                certificate.display_title = certificate.title_en
                certificate.display_description = certificate.description_en
        
        return context
