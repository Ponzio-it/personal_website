# Generated by Django 5.1.2 on 2024-12-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_remove_blogpost_featured_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Master', 'Master'), ('PhD', 'PhD'), ('Other', 'Other')], help_text="Degree type (e.g., Bachelor's, Master's).", max_length=50, verbose_name='Degree'),
        ),
    ]
