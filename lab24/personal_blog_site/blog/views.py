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
    context = {
        'category': category
    }
    return render(request, 'category_detail.html', context)


class BlogView(View):
    template_name = 'blog_index.html'

    def get(self, request):
        print(self.request)
        blogs = Category.objects.all()
        context = {
            'blogs': blogs
        }
        return render(request, self.template_name, context)
