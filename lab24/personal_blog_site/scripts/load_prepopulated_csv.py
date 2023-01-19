from blog.models import Blog, Category
import csv


def import_csv_data(reader, model):
    next(reader)  # skips header
    for row in reader:
        new_model = model(*row)
        new_model.save()


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


def run():
    with open('scripts/csv/category.csv') as category_file, open('scripts/csv/blog.csv') as blog_file:
        category_reader = csv.reader(category_file)
        blog_reader = csv.reader(blog_file)

        Blog.objects.all().delete()
        Category.objects.all().delete()

        import_csv_data(category_reader, Category)
        import_csv_data(blog_reader, Blog)
        import_blog_category()


if __name__ == "__main__":
    run()
