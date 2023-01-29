# Generated by Django 4.1.5 on 2023-01-17 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_themeblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('entry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.entry')),
            ],
        ),
    ]
