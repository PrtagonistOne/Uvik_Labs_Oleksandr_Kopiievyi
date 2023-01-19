from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogView.as_view(), name='main_blog_page'),
    path('<int:pk>', views.BlogView.as_view(), name='blog_detail')
]
