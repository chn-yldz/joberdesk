# Generated by Django 4.0.1 on 2022-07-31 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0013_post_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='businesses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.business'),
        ),
    ]