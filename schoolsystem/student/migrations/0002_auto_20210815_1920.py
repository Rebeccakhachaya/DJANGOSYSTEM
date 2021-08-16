# Generated by Django 3.2.4 on 2021-08-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image_of_the_student',
        ),
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='health_records',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
