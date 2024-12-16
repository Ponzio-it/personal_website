# Generated by Django 5.1.2 on 2024-12-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_remove_blogpost_content_remove_blogpost_excerpt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name_en',
            field=models.CharField(help_text='The name of the skill in English (e.g., Python, Data Analysis).', max_length=100, verbose_name='Name (EN)'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name_it',
            field=models.CharField(help_text='The name of the skill in Italian (e.g., Python, Analisi dei dati).', max_length=100, verbose_name='Name (IT)'),
        ),
    ]