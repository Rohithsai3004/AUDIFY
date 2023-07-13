# Generated by Django 4.1.5 on 2023-06-20 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_videolinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200)),
                ('timestamps', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('video_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.videolinks')),
            ],
        ),
    ]
