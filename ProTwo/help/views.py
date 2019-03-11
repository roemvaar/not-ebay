from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'dinosaurio': 'CALLLEEEEESSE VIEJO LESBIANO'}
    return render(request, 'help/help.html', context=my_dict)
