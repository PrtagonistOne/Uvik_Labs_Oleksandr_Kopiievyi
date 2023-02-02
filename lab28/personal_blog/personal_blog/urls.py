"""personal_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView

from post.urls import post_router
from blog.urls import blog_router

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

main_router = routers.DefaultRouter()
main_router.registry.extend(post_router.registry)
main_router.registry.extend(blog_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(main_router.urls)),
    path("", include("post.urls")),
]

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
