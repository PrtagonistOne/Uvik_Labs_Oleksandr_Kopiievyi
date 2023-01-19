from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_index, name='welcome_page'),
    path('<int:pk>', views.user_detail, name='user_detail')
]
