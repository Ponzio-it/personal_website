# Generated by Django 5.1.2 on 2024-11-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Job title (e.g., Software Developer)', max_length=255)),
                ('company', models.CharField(help_text='Company name', max_length=255)),
                ('start_date', models.DateField(help_text='Start date of the job')),
                ('end_date', models.DateField(blank=True, help_text='End date of the job (if applicable)', null=True)),
                ('description', models.TextField(blank=True, help_text='Description of responsibilities or achievements')),
                ('skills', models.ManyToManyField(blank=True, help_text='Skills related to this job experience', related_name='job_experiences', to='portfolio.skill')),
            ],
        ),
    ]
