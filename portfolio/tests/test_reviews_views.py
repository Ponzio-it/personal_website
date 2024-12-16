from django.urls import reverse
from django.test import TestCase
from portfolio.models import Project, Review
from django.utils import timezone


class ProjectDetailViewTest(TestCase):
    def setUp(self):
        # Create a project and reviews associated with it
        self.project = Project.objects.create(
            title_en="Sample Project",
            title_it="Progetto di esempio",
            description_en="Description for sample project.",
            description_it="Descrizione per il progetto di esempio.",
            date=timezone.now().date(),
            technologies="Django, Python",
            public_url="https://github.com/example/sample-project",
            is_public=True
        )
        # Create two reviews: one approved, one pending
        self.approved_review = Review.objects.create(
            project=self.project,
            reviewer_name="Approved User",
            content="This is an approved review.",
            recommendation=True,
            status='approved'
        )
        self.pending_review = Review.objects.create(
            project=self.project,
            reviewer_name="Pending User",
            content="This is a pending review.",
            recommendation=False,
            status='pending'
        )

    def test_only_approved_reviews_displayed(self):
        """Test that only approved reviews are displayed on the project detail page."""
        response = self.client.get(reverse('portfolio:project_detail', args=[self.project.pk]))
        reviews = response.context['reviews']
        self.assertIn(self.approved_review, reviews)
        self.assertNotIn(self.pending_review, reviews)


class ReviewCreateViewTest(TestCase):
    def setUp(self):
        # Create a project to associate with the review
        self.project = Project.objects.create(
            title_en="Test Project for Review",
            title_it="Progetto di test per la revisione",
            description_en="Description for review test project.",
            description_it="Descrizione per il progetto di test della revisione.",
            date=timezone.now().date(),
            technologies="Django, Python",
            public_url="https://github.com/example/test-project-review",
            is_public=True
        )

    def test_review_submission(self):
        """Test that a review can be submitted and saved with a 'pending' status."""
        form_data = {
            'reviewer_name': "New Reviewer",
            'content': "Great project!",
            'recommendation': True,
        }
        response = self.client.post(
            reverse('portfolio:project_review', args=[self.project.pk]),
            data=form_data
        )

        # Confirm redirect after submission
        self.assertRedirects(response, reverse('portfolio:project_detail', args=[self.project.pk]))

        # Check if the review was saved with 'pending' status
        review = Review.objects.get(reviewer_name="New Reviewer")
        self.assertEqual(review.project, self.project)
        self.assertEqual(review.content, "Great project!")
        self.assertTrue(review.recommendation)
        self.assertEqual(review.status, 'pending')
