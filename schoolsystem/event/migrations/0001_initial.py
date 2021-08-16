# Generated by Django 3.2.4 on 2021-08-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=12, null=True)),
                ('venue', models.CharField(max_length=12)),
                ('agenda', models.CharField(max_length=12)),
                ('date_of_the_event', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('description', models.CharField(max_length=12)),
                ('event_link', models.CharField(max_length=12)),
            ],
        ),
    ]
