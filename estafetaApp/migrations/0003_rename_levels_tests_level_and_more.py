# Generated by Django 4.0.6 on 2022-09-02 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estafetaApp', '0002_rename_date_stat_tests_date_start_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tests',
            old_name='levels',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='tests',
            old_name='subjects',
            new_name='subject',
        ),
    ]
