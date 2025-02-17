# Generated by Django 5.1.2 on 2024-12-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_remove_certificate_image_certificate_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='featured_image_url',
            field=models.URLField(blank=True, help_text='Optional URL for the featured image of the blog post.', null=True, verbose_name='Featured Image URL'),
        ),
    ]
