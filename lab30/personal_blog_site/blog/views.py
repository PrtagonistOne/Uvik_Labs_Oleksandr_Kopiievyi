from django.shortcuts import render
from django.views import View

from .models import Category, Blog


def category_index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category_index.html', context)


def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    blog = Blog.objects.all().filter(category=category)
    context = {
        'category': category,
        'blog': blog
    }
    return render(request, 'category_detail.html', context)


class BlogView(View):
    template_name = 'blog_index.html'

    def get(self, request, pk=None):
        if pk is None:
            blogs = Blog.objects.all()
            return render(request, self.template_name, {'blogs': blogs})
        blog = Blog.objects.get(pk=pk)
        categories = Category.objects.all().filter(blog=blog)
        return render(request, 'blog_detail.html', {'blog': blog, 'categories': categories})
