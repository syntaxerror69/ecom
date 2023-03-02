from django.shortcuts import render,redirect
from .models import *
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login as LoginForm, logout



# Create your views here.



def homepage(r):
        
    categoryData = Category.objects.all()
    productData = Product.objects.all()
    data = {
        'categoryData': categoryData,
        'productData': productData
    }

    # data['category'] = getCategory()
    return render(r, 'home.html', data)

def categoryWise(r,slug):
    # data = {}
    # data['category'] = Category.objects.all()
    # data['products'] = Product.objects.filter(category__slug=slug)
    # return render(r,'home.html',data)
    categoryData = Category.objects.all()
    productData = Product.objects.filter(category__slug=slug)

    data = {
        'categoryData': categoryData,
        'productData': productData
    }
    return render(r, 'home.html', data)

def search(r):
    data={}
    data['category'] = Category.objects.all()
    data['products'] = Product.objects.filter(name__icontains=r.GET.get('search'))
    return render(r, 'home.html',data)

def viewProduct(r, slug):
    data = {}
    data['category'] = Category.objects.all()
    data['product'] = Product.objects.get(slug=slug)
    return render(r, 'singleView.html',data)


def register(r):
    form = RegisterForm(r.POST or None)
    if r.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(login)
    data = {}
    data['form'] = form
    return render(r, 'register.html', data)

def login(r):
    form = AuthenticationForm(r.POST or None)
    if r.method == 'POST':
        #  if form.is_valid():
            username = r.POST.get('username')
            password = r.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                LoginForm(r,user)
                return redirect(homepage)

    data = {}
    data['form'] = form
    return render(r, 'login.html', data)
   


def logoutForm(r):
    logout(r)
    return redirect(login)             