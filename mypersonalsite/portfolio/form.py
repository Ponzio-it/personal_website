from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for users to submit a review for a project.
    """
    class Meta:
        model = Review
        fields = ['reviewer_name', 'content', 'recommendation']
        labels = {
            'reviewer_name': _('Your Name'),
            'content': _('Your Review'),
            'recommendation': _('Would you recommend this project?'),
        }
        help_texts = {
            'reviewer_name': _('Enter your full name.'),
            'content': _('Write your honest feedback about the project.'),
            'recommendation': _('Select Yes or No.'),
        }


class ContactForm(forms.Form):
    """
    Form to collect contact details from users.
    """
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': _('First Name')}),
        label=_('First Name'),
        help_text=_("Enter your first name."),
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': _('Last Name')}),
        label=_('Last Name'),
        help_text=_("Enter your last name."),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': _('Your Email')}),
        label=_('Email'),
        help_text=_("Enter a valid email address."),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': _('Your Message')}),
        label=_('Message'),
        help_text=_("Enter your message here."),
    )
