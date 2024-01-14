# Generated by Django 4.2.6 on 2024-01-13 06:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserSite', '0011_borrow_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrow_history',
            old_name='post',
            new_name='book',
        ),
        migrations.AlterField(
            model_name='borrow_history',
            name='borrow_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]