# Generated by Django 5.1.3 on 2024-11-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
