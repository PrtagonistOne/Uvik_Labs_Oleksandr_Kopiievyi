from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from .views import my_view

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('your-name/', views.get_name, name='name'),
    path('your-name/thanks/', views.ThanksView.as_view(), name='thanks'),
    path('get_contact/', views.get_contact, name='thanks'),
    path('foo/<int:code>/', cache_page(60 * 15)(my_view)),

]
