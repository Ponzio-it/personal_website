# Generated by Django 5.1.2 on 2024-11-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_category_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='github_url',
            field=models.URLField(blank=True, help_text='GitHub profile URL of the site owner.', null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='linkedin_url',
            field=models.URLField(blank=True, help_text='LinkedIn profile URL of the site owner.', null=True),
        ),
    ]
