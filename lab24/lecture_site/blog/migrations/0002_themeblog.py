# Generated by Django 4.1.5 on 2023-01-17 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeBlog',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.blog')),
                ('theme', models.CharField(max_length=200)),
            ],
            bases=('blog.blog',),
        ),
    ]
