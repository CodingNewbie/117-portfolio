# Generated by Django 5.0.6 on 2024-06-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='content.technology'),
        ),
    ]
