# Generated by Django 5.1.2 on 2024-11-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publised_date',
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateField(auto_now=True),
        ),
    ]
