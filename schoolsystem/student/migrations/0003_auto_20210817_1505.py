# Generated by Django 3.2.4 on 2021-08-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210815_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_year',
            field=models.DateField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent_contact',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
