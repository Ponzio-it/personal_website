# Generated by Django 5.1.2 on 2024-12-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_skill_name_en_alter_skill_name_it'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='name_it',
        ),
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(default='python', help_text='The name of the skill (e.g., Python, Data Analysis).', max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
    ]