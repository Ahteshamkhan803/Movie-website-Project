# Generated by Django 5.0.6 on 2024-06-07 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_App', '0002_remove_movies_model_movies_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_model',
            name='Review_Movie_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reviews', to='Movie_App.movies_model'),
        ),
    ]
