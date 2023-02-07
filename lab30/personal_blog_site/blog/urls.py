from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 15)(views.BlogView.as_view()), name='main_blog_page'),
    path('<int:pk>', cache_page(60 * 15)(views.BlogView.as_view()), name='blog_detail'),
    path('categories/', cache_page(60 * 15)(views.category_index), name='main_category_page'),
    path('categories/<int:pk>/', cache_page(60 * 15)(views.category_detail), name='category_detail')

]
