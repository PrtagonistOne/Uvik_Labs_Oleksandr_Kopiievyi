from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='main_blog_page'),
    path('<int:pk>', views.BlogView.as_view(), name='blog_detail'),
    path('categories/', views.category_index, name='main_category_page'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail')

]
