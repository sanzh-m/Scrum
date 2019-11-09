# Generated by Django 2.2.7 on 2019-11-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprintbacklog',
            name='index',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='sprintbacklog',
            constraint=models.UniqueConstraint(fields=('index', 'project'), name='unique_sprint'),
        ),
    ]
