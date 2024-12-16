from django.test import TestCase
from portfolio.models import BlogPost, Category


class BlogModelTest(TestCase):
    def setUp(self):
        """Set up a sample category and blog post for testing the Blog model."""
        self.category = Category.objects.create(
            name_en="Technology", 
            name_it="Tecnologia", 
            slug="technology"
        )
        
        self.post = BlogPost.objects.create(
            title_en="Sample Blog Post", 
            title_it="Post del blog di esempio", 
            content_en="This is a sample blog post content.", 
            content_it="Questo è un contenuto di esempio per il post del blog.", 
            author="John Doe"
        )
        self.post.categories.add(self.category)

    def test_category_creation(self):
        """Test that a category is created correctly."""
        self.assertEqual(self.category.name_en, "Technology")
        self.assertEqual(self.category.slug, "technology")

    def test_blog_post_creation(self):
        """Test that a blog post is created correctly."""
        self.assertEqual(self.post.title_en, "Sample Blog Post")
        self.assertIn(self.category, self.post.categories.all())

    def test_blog_post_slug_generation(self):
        """Test that the blog post's slug is correctly generated."""
        self.assertEqual(self.post.slug, "sample-blog-post")

    def test_blog_post_str_representation(self):
        """Test the string representation of the blog post."""
        self.assertEqual(str(self.post), "Sample Blog Post")
