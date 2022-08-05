# Generated by Django 4.0.6 on 2022-08-05 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripOApp', '0012_remove_profile_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='tripOApp.trip'),
            preserve_default=False,
        ),
    ]