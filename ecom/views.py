from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Products, Cart
# Create your views here.

def home(request):

    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'ecom/home.html', context)

def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'ecom/login.html', context)

def userLogout(request):
    logout(request)
    return redirect('home')


def userRegister(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    return render(request, 'ecom/register.html', {'form': form})

def addToCart(request, pk):

    if request.method == 'POST':
        user = request.user
        product = Products.objects.get(id=pk)
        cart_item, add = Cart.objects.get_or_create(owner=user, item=product)

        if not add:
         cart_item.quantity += 1
         cart_item.save()

    return redirect('home')

def removeItem(request, pk):

    if request.method == 'POST':
        item = Cart.objects.get(id=pk)

        if item.quantity is not 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

    return redirect('home')

def uploadProduct(request):

    if request.method == 'POST':
        pname = request.POST.get('prod_name')
        pimage = request.POST.get('prod_image')
        type = request.POST.get('prod_type')
        price = request.POST.get('prod_price')

        prod = Products.objects.create(pname=pname, pimage=pimage, type=type, price=price)

    context = {}
    return render(request, 'ecom/upload.html', context)

def myCart(request, pk):

    items = Cart.objects.all()
    total = 0

    for item in items:
        if item.owner.username == request.user.username:
            price = item.item.price
            total += price

    context = {'items': items, 'total': total}
    return render(request, 'ecom/mycart.html', context)

