from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from portfolio.models import BlogPost, Category


class BlogViewTest(TestCase):
    def setUp(self):
        """Set up categories and blog posts for testing the blog views."""
        self.category = Category.objects.create(
            name_en="Technology", 
            name_it="Tecnologia"
        )
        
        image = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
        
        self.post = BlogPost.objects.create(
            title_en="Sample Blog Post", 
            title_it="Post del blog di esempio", 
            content_en="This is a sample blog post content.", 
            content_it="Questo è un contenuto di esempio per il post del blog.", 
            author="John Doe", 
            featured_image=image
        )
        self.post.categories.add(self.category)

    def test_blog_list_view(self):
        """Test the blog list view."""
        response = self.client.get(reverse('portfolio:blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/blog_list.html')
        self.assertContains(response, "Sample Blog Post")
        self.assertContains(response, "Technology")

    def test_blog_list_view_with_search(self):
        """Test the blog list view with a search query."""
        response = self.client.get(reverse('portfolio:blog_list'), {'q': 'Sample'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Blog Post")

    def test_blog_detail_view(self):
        """Test the blog detail view."""
        response = self.client.get(reverse('portfolio:blog_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/blog_detail.html')
        self.assertContains(response, "Sample Blog Post")
        self.assertContains(response, "This is a sample blog post content.")


class BlogEdgeCaseTest(TestCase):
    def test_blog_detail_view_nonexistent_post(self):
        """Test accessing a blog detail page that does not exist."""
        response = self.client.get(reverse('portfolio:blog_detail', args=['nonexistent-post']))
        self.assertEqual(response.status_code, 404)

    def test_blog_list_view_no_posts(self):
        """Test the blog list view when no posts exist."""
        response = self.client.get(reverse('portfolio:blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts found.")
