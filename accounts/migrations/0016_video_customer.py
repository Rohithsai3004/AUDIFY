# Generated by Django 4.1.5 on 2023-06-20 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
        ),
    ]
