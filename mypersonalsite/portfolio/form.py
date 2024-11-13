from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """
    Form for users to submit a review for a project.
    """

    class Meta:
        model = Review
        fields = ['reviewer_name', 'content', 'recommendation']
