# Generated by Django 3.0.8 on 2020-07-30 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='client_message',
        ),
    ]
