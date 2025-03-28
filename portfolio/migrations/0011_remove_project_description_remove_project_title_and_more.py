# Generated by Django 5.1.2 on 2024-12-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_blogpost_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title',
        ),
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(default='default description', help_text='Detailed description of the project in English.', verbose_name='Description (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='description_it',
            field=models.TextField(default='descrizione', help_text='Detailed description of the project in Italian.', verbose_name='Description (IT)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.CharField(default='progetto', help_text='Title of the project in English.', max_length=100, verbose_name='Title (EN)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title_it',
            field=models.CharField(default='project', help_text='Title of the project in Italian.', max_length=100, verbose_name='Title (IT)'),
            preserve_default=False,
        ),
    ]
