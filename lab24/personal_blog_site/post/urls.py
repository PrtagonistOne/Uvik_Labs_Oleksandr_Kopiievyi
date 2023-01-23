from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='main_post_page'),
    path('<int:pk>', views.PostView.as_view(), name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_comment/<int:pk>/', views.CommentCreateFormView.as_view(), name='create_comment'),
    path('delele_comment/<int:pk>/', views.CommentDeleteView.as_view(), name='delete_comment')
]
