from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60*15)(views.user_index), name='welcome_page'),
    path('<int:pk>', cache_page(60*15)(views.user_detail), name='user_detail'),
]
