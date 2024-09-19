from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from shops import forms
from shops.models import Product, Category


def Viewmain(request):
    all_products = Product.objects.all()
    return render(request, 'shops/index.html', {'products': all_products})


def AboutUs(request):
    return render(request, 'shops/AboutUs.html')


def Login_User(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"خوش اومدی{username}")
            return redirect('main')
        else:
            messages.success(request, 'با دقت وارد شو و اگر ثبت نام نکردی ،بدو ثبت نام کن!!')
            return redirect('login')
    else:
        return render(request, 'shops/login.html')


def Logout_User(request):
    logout(request)
    messages.success(request, 'همینو میخواستی؟؟ خارج شدی')
    return redirect("main")


# Create your views here.
def sign_info(request):
    if request.method == 'POST':
        formregister = forms.RegisterForm(request.POST)
        if formregister.is_valid():
            data = formregister.cleaned_data
            User.objects.create_user(username=data['user_name'], email=data['Email'], password=data['password2'])
            user = authenticate(request, username=data['user_name'], password=data['password2'])
            login(request, user)
            return redirect('main')
    else:
        formregister = forms.RegisterForm()
    return render(request, 'shops/sign-in.html', {'formregister': formregister})


def product_details(request, s):
    product = Product.objects.get(slug=s)
    return render(request, 'shops/product_details.html', {'product': product})


def product_category(request, s):
    try:
        category = Category.objects.get(slug=s)
        product = Product.objects.filter(category=category)
        return render(request, "shops/Category.html", {'category': category, 'product': product})
    except:
        messages.success(request, ("این دسته بندی رو نداریم که!!!!"))
        return redirect("main")


def category(request):
    categories = Category.objects.all()

    return render(request, "shops/categories.html", {'categories':categories })
