import csv

from blog.models import Blog, Category
from user.models import User
from post.models import Post, Comment

from django.core.management.color import no_style
from django.db import connection

from user.managers import CustomUserManager


def import_csv_data(dict_reader, model):
    data_dict = list(dict_reader)
    for datum in data_dict:
        new_model_row = model(**datum)
        new_model_row.save()


def import_user_data(user_dict_reader: dict, model: CustomUserManager):
    data_dict = list(user_dict_reader)

    for datum in data_dict:
        if datum.get('is_superuser') is not True:
            new_model_row = model.objects.create_user(**datum)
        else:
            new_model_row = model.objects.create_superuser(**datum)
        new_model_row.save()


def import_blog_category():
    with open('scripts/csv/blog_category.csv') as blog_category_file:
        blog_category_reader = csv.reader(blog_category_file)
        next(blog_category_reader)
        for row in blog_category_reader:
            blog_id = row[0]
            category_id = row[1]

            blog = Blog.objects.get(pk=blog_id)
            category = Category.objects.get(pk=category_id)

            blog.category.add(category)


def clean_db_date() -> None:
    Post.objects.all().delete()
    Comment.objects.all().delete()
    User.objects.all().delete()
    Blog.objects.all().delete()
    Category.objects.all().delete()


def run():
    clean_db_date()
    with open('scripts/csv/category.csv') as category_file, open('scripts/csv/blog.csv') as blog_file:
        category_reader = csv.DictReader(category_file)
        blog_reader = csv.DictReader(blog_file)

        import_csv_data(category_reader, Category)
        import_csv_data(blog_reader, Blog)
        import_blog_category()
    with open('scripts/csv/user.csv') as user_file:
        user_reader = csv.DictReader(user_file)

        import_user_data(user_reader, User)
    with open('scripts/csv/post.csv') as post_file, open('scripts/csv/comment.csv') as comment_file:
        post_reader = csv.DictReader(post_file)
        comment_reader = csv.DictReader(comment_file)

        updated_post_data = []
        for post in post_reader:
            for key, value in post.items():
                if key == 'user':
                    post[key] = User.objects.get(pk=value)
                if key == 'blog':
                    post[key] = Blog.objects.get(pk=value)
            updated_post_data.append(post)
        import_csv_data(updated_post_data, Post)

        updated_comment_data = []
        for comment in comment_reader:
            for key, value in comment.items():
                if key == 'post':
                    comment[key] = Post.objects.get(pk=value)
            updated_comment_data.append(comment)
        import_csv_data(updated_comment_data, Comment)

    sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Comment, Post,
                                                                  User, Blog, Category])
    with connection.cursor() as cursor:
        for sql in sequence_sql:
            cursor.execute(sql)


if __name__ == "__main__":
    run()
