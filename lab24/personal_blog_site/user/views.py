from django.shortcuts import render

from .models import User


def user_index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user_index.html', context)


def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'user_detail.html', context)
