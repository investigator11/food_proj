# Generated by Django 4.1 on 2022-09-10 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emal',
            new_name='email',
        ),
    ]
