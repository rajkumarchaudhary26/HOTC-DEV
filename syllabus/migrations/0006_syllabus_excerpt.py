# Generated by Django 4.0.5 on 2022-06-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0005_alter_syllabus_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabus',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]