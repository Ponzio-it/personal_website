# Generated by Django 5.1.2 on 2024-12-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_remove_project_onedrive_file_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
        migrations.AddField(
            model_name='file',
            name='file_url',
            field=models.URLField(default='e', help_text='URL to the file hosted on Cloud.', max_length=500, verbose_name='file Link'),
            preserve_default=False,
        ),
    ]
