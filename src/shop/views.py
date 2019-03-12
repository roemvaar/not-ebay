from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from shop.forms import UserForm, ProductForm
from shop.models import Product


def index(request):
    return render(request, 'shop/index.html')


def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'shop/registration.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request, 'shop/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def sell_item(request):
    if request.method == 'POST':
        newproduct_form = ProductForm(data=request.POST)

        if newproduct_form.is_valid():
            new_product = newproduct_form.save()

    return render(request, 'shop/sell_item.html', {'newproduct_form': newproduct_form})


def buy(request):
    product_list = Product.objects.order_by('date')
    return render(request, 'shop/buy.html', {'product_list': product_list})
