# Generated by Django 2.2.6 on 2019-11-05 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBacklog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBacklogItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('size', models.DecimalField(decimal_places=0, max_digits=3)),
                ('status', models.CharField(max_length=20)),
                ('pb_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.ProductBacklog')),
            ],
        ),
    ]
