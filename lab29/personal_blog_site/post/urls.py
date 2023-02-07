from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 15)(views.PostView.as_view()), name='main_post_page'),
    path('<int:pk>', views.PostView.as_view(), name='post_detail'),
    path('create_comment/<int:pk>/', views.CommentCreateFormView.as_view(), name='create_comment'),
    path('delele_comment/<int:pk>/', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('update_comment/<int:pk>/', views.CommentUpdateView.as_view(), name='update_comment')
]
