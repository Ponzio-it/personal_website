from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Project, Review
from django.utils import timezone


class ReviewAdminTest(TestCase):
    def setUp(self):
        # Set up admin user and login
        self.admin_user = User.objects.create_superuser(
            username='admin', 
            password='admin123', 
            email='admin@example.com'
        )
        self.client = Client()
        self.client.login(username='admin', password='admin123')

        # Create a project and a review for testing admin actions
        self.project = Project.objects.create(
            title_en="Admin Test Project",
            title_it="Progetto di Test Amministratore",
            description_en="Project for testing admin actions.",
            description_it="Progetto per testare le azioni dell'amministratore.",
            date=timezone.now().date(),
            technologies="Django, Testing",
            public_url="https://github.com/example/admin-test-project",
            is_public=True
        )
        self.review = Review.objects.create(
            project=self.project,
            reviewer_name="Admin Reviewer",
            content="This is a test review for admin actions.",
            recommendation=True,
            status='pending'
        )

    def test_approve_review_action(self):
        """Test that the admin can approve a review using the admin action."""
        url = reverse('admin:portfolio_review_changelist')
        response = self.client.post(url, {'action': 'approve_reviews', '_selected_action': [self.review.pk]})
        
        # Reload the review from the database
        self.review.refresh_from_db()
        
        # Verify the review status was updated to 'approved'
        self.assertEqual(self.review.status, 'approved')

    def test_reject_review_action(self):
        """Test that the admin can reject a review using the admin action."""
        url = reverse('admin:portfolio_review_changelist')
        response = self.client.post(url, {'action': 'reject_reviews', '_selected_action': [self.review.pk]})
        
        # Reload the review from the database
        self.review.refresh_from_db()
        
        # Verify the review status was updated to 'rejected'
        self.assertEqual(self.review.status, 'rejected')
