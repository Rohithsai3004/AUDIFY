# Generated by Django 4.1.5 on 2023-06-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
