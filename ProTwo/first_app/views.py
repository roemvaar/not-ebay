from django.shortcuts import render
from first_app.models import User


def index(request):
    my_dict = {'name': 'Roberto'}
    return render(request, 'first_app/index.html', context=my_dict)


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'first_app/users.html', context=user_dict)
