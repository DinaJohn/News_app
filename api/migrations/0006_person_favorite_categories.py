# Generated by Django 4.2.6 on 2023-12-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_category_newsarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='favorite_categories',
            field=models.ManyToManyField(blank=True, to='api.category'),
        ),
    ]