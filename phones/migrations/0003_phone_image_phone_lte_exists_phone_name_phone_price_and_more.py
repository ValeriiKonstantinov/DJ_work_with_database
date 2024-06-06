# Generated by Django 5.0.4 on 2024-06-01 10:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_remove_phone_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.URLField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
    ]