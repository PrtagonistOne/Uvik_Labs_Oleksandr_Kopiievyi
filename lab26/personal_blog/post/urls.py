from django.urls import path
from rest_framework import routers
from post import views

post_router = routers.DefaultRouter()
post_router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('users/', views.get_all_users),
    path('users/<int:pk>', views.RetrieveUser.as_view())
]
