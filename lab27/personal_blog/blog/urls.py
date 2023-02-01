from rest_framework import routers
from blog import views

blog_router = routers.DefaultRouter()
blog_router.register(r'blogs', views.BlogViewSet, basename='blog')

