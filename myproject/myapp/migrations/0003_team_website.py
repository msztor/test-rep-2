# Generated by Django 5.1.3 on 2024-11-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_person_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='website',
            field=models.URLField(null=True),
        ),
    ]