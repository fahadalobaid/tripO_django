# Generated by Django 4.0.6 on 2022-08-05 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripOApp', '0013_profile_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='trip',
        ),
        migrations.AddField(
            model_name='trip',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='tripOApp.profile'),
            preserve_default=False,
        ),
    ]