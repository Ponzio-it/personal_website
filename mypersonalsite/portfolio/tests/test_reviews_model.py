from django.test import TestCase
from django.utils import timezone
from portfolio.models import Project, Review

class ReviewModelTest(TestCase):
    def setUp(self):
        # Create a sample project to associate with the review
        self.project = Project.objects.create(
            title="Test Project",
            description="Description for test project.",
            date=timezone.now().date(),
            technologies="Django, Python",
            public_url="https://github.com/example/test-project",
            is_public=True
        )

    def test_review_creation(self):
        # Create a review instance
        review = Review.objects.create(
            project=self.project,
            reviewer_name="John Doe",
            content="Great project! Highly recommended.",
            recommendation=True,
            status='pending'  # Default status set to 'pending'
        )
        # Check if review is created and fields are set correctly
        self.assertEqual(review.project, self.project)
        self.assertEqual(review.reviewer_name, "John Doe")
        self.assertEqual(review.content, "Great project! Highly recommended.")
        self.assertTrue(review.recommendation)
        self.assertEqual(review.status, 'pending')
