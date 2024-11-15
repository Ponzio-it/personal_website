from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for users to submit a review for a project.
    """

    class Meta:
        model = Review
        fields = ['reviewer_name', 'content', 'recommendation']


class ContactForm(forms.Form):
    """
    Form to collect contact details from users.
    """
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First Name'}), help_text="Enter your first name.")
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),help_text="Enter your last name.")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}),help_text="Enter a valid email address.")
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}),help_text="Enter your message here.")
