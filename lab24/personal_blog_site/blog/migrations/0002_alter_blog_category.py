# Generated by Django 4.1.5 on 2023-01-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='Categories'),
        ),
    ]