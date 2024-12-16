# Generated by Django 5.1.2 on 2024-12-13 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_remove_project_description_remove_project_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='description',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='field',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='title',
        ),
        migrations.RemoveField(
            model_name='education',
            name='description',
        ),
        migrations.RemoveField(
            model_name='education',
            name='field_of_study',
        ),
        migrations.RemoveField(
            model_name='education',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='name',
        ),
        migrations.RemoveField(
            model_name='jobexperience',
            name='description',
        ),
        migrations.RemoveField(
            model_name='jobexperience',
            name='title',
        ),
        migrations.RemoveField(
            model_name='section',
            name='description',
        ),
        migrations.RemoveField(
            model_name='section',
            name='title',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='name',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content_en',
            field=models.TextField(default='lore ipsum eng', help_text='Main content of the blog post in English.', verbose_name='Content (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content_it',
            field=models.TextField(default='lore ipsum it', help_text='Main content of the blog post in Italian.', verbose_name='Content (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='excerpt_en',
            field=models.TextField(blank=True, help_text='Short summary or excerpt of the blog post in English.', verbose_name='Excerpt (EN)'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='excerpt_it',
            field=models.TextField(blank=True, help_text='Short summary or excerpt of the blog post in Italian.', verbose_name='Excerpt (IT)'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title_en',
            field=models.CharField(default='title eng', help_text='Title of the blog post in English.', max_length=200, verbose_name='Title (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title_it',
            field=models.CharField(default='title it', help_text='Title of the blog post in Italian.', max_length=200, verbose_name='Title (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(default='name eng', help_text='Name of the category in English.', max_length=100, verbose_name='Name (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='name_it',
            field=models.CharField(default='name it', help_text='Name of the category in Italian.', max_length=100, verbose_name='Name (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='description_en',
            field=models.TextField(default='lore ipsum eng', help_text='Description of the course in English.', verbose_name='Description (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='description_it',
            field=models.TextField(default='lore ipsum it', help_text='Description of the course in Italian.', verbose_name='Description (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='title_en',
            field=models.CharField(default='title eng', help_text='The title of the certificate in English.', max_length=255, verbose_name='Title (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificate',
            name='title_it',
            field=models.CharField(default='title it', help_text='The title of the certificate in Italian.', max_length=255, verbose_name='Title (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='description_en',
            field=models.TextField(blank=True, help_text='Optional description of the program or notable achievements in English.', verbose_name='Description (EN)'),
        ),
        migrations.AddField(
            model_name='education',
            name='description_it',
            field=models.TextField(blank=True, help_text='Optional description of the program or notable achievements in Italian.', verbose_name='Description (IT)'),
        ),
        migrations.AddField(
            model_name='education',
            name='field_of_study_en',
            field=models.CharField(default='master eng', help_text='Field of study in English (e.g., Computer Science).', max_length=255, verbose_name='Field of Study (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='field_of_study_it',
            field=models.CharField(default='master it', help_text='Field of study in Italian (e.g., Informatica).', max_length=255, verbose_name='Field of Study (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='institution_en',
            field=models.CharField(default='institution eng', help_text='Name of the educational institution in English.', max_length=255, verbose_name='Institution (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='institution_it',
            field=models.CharField(default='institurion it', help_text='Name of the educational institution in Italian.', max_length=255, verbose_name='Institution (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='name_en',
            field=models.CharField(default='name eng', help_text="Name of the file in English, e.g., 'Project_Plan.pdf'.", max_length=100, verbose_name='Name (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='name_it',
            field=models.CharField(default='name it', help_text="Name of the file in Italian, e.g., 'Piano_Progetto.pdf'.", max_length=100, verbose_name='Name (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='name_en',
            field=models.CharField(default='name eng', help_text="Name of the folder in English, e.g., 'Documentation'.", max_length=100, verbose_name='Name (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='name_it',
            field=models.CharField(default='name it', help_text="Name of the folder in Italian, e.g., 'Documentazione'.", max_length=100, verbose_name='Name (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobexperience',
            name='description_en',
            field=models.TextField(blank=True, help_text='Description of responsibilities or achievements in English', verbose_name='Description (EN)'),
        ),
        migrations.AddField(
            model_name='jobexperience',
            name='description_it',
            field=models.TextField(blank=True, help_text='Description of responsibilities or achievements in Italian', verbose_name='Description (IT)'),
        ),
        migrations.AddField(
            model_name='jobexperience',
            name='title_en',
            field=models.CharField(default='title eng', help_text='Job title in English (e.g., Software Developer)', max_length=255, verbose_name='Title (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobexperience',
            name='title_it',
            field=models.CharField(default='title it', help_text='Job title in Italian (e.g., Sviluppatore Software)', max_length=255, verbose_name='Title (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='description_en',
            field=models.TextField(default='lore ipsum eng', help_text='Description content for the section in English', verbose_name='Description (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='description_it',
            field=models.TextField(default='lore ipsum it', help_text='Description content for the section in Italian', verbose_name='Description (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='title_en',
            field=models.CharField(default='title eng', help_text='Title of the section in English', max_length=200, verbose_name='Title (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='title_it',
            field=models.CharField(default='title it', help_text='Title of the section in Italian', max_length=200, verbose_name='Title (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='name_en',
            field=models.CharField(default='name eng', help_text='The name of the skill in English (e.g., Python, Data Analysis).', max_length=100, verbose_name='Name (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='name_it',
            field=models.CharField(default='name it', help_text='The name of the skill in Italian (e.g., Python, Analisi dei dati).', max_length=100, verbose_name='Name (IT)'),
            preserve_default=False,
        ),
    ]
