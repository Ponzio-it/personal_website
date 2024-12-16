from django.test import TestCase
from django.utils import timezone
from portfolio.models import Project, Review


class ReviewModelTest(TestCase):
    def setUp(self):
        # Create a sample project to associate with the review
        self.project = Project.objects.create(
            title_en="Test Project",
            title_it="Progetto di Test",
            description_en="Description for test project.",
            description_it="Descrizione per il progetto di test.",
            date=timezone.now().date(),
            technologies="Django, Python",
            public_url="https://github.com/example/test-project",
            is_public=True
        )

    def test_review_creation(self):
        """Test that a review can be created and its fields are set correctly."""
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
