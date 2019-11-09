# Generated by Django 2.2.6 on 2019-11-07 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SprintBacklog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('availableEffort', models.DecimalField(decimal_places=0, max_digits=3)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('effort', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('NS', 'Not Started'), ('DI', 'Development In Progress'), ('DD', 'Development Done'), ('TI', 'Testing In Process'), ('TD', 'Testing Done'), ('DO', 'Done')], default='NS', max_length=2, null=True)),
                ('description', models.CharField(max_length=500)),
                ('index', models.PositiveIntegerField()),
                ('PBI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.ProductBacklogItem')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Developer')),
                ('sprint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sprints.SprintBacklog')),
            ],
        ),
        migrations.AddConstraint(
            model_name='task',
            constraint=models.UniqueConstraint(fields=('index', 'PBI'), name='unique_task'),
        ),
    ]
