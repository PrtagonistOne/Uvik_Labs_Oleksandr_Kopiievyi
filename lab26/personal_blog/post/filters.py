from django.contrib.auth.models import User
from django_filters import AllValuesFilter, DateTimeFilter
from django_filters.rest_framework import FilterSet


class UserFilter(FilterSet):
    username = AllValuesFilter(field_name='username')
    first_name = AllValuesFilter(field_name='first_name')
    days_joined = DateTimeFilter(field_name='date_joined',
                                 lookup_expr='gte')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'date_joined')
