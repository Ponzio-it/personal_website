# Generated by Django 5.1.1 on 2024-11-18 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_contactinfo_github_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the section', max_length=200)),
                ('description', models.TextField(help_text='Description content for the section')),
            ],
        ),
    ]