# Generated by Django 2.2.6 on 2019-11-02 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('sprints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbi',
            name='sprint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sprints.SprintBacklog'),
        ),
    ]