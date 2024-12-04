from django.test import TestCase
from ..models import BlogPost, Category


class BlogModelTest(TestCase):
    def setUp(self):
        # Set up a sample category
        self.category = Category.objects.create(name="Technology")
        # Set up a sample blog post
        self.post = BlogPost.objects.create(
            title="Sample Blog Post",
            content="This is a sample blog post content.",
            author="John Doe",
        )
        self.post.categories.add(self.category)

    def test_category_creation(self):
        """Test that a category is created correctly."""
        self.assertEqual(self.category.name, "Technology")
        self.assertEqual(self.category.slug, "technology")

    def test_blog_post_creation(self):
        """Test that a blog post is created correctly."""
        self.assertEqual(self.post.title, "Sample Blog Post")
        self.assertEqual(self.post.slug, "sample-blog-post")
        self.assertIn(self.category, self.post.categories.all())

    def test_blog_post_str_representation(self):
        """Test the string representation of the blog post."""
        self.assertEqual(str(self.post), "Sample Blog Post")
