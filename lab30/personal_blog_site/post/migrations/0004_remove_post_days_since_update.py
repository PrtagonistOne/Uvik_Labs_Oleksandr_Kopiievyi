# Generated by Django 4.1.5 on 2023-01-26 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_days_since_update_alter_comment_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='days_since_update',
        ),
    ]
