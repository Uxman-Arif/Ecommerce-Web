from django.http import HttpResponse
from django.shortcuts import render, redirect
from collections import defaultdict 
from ecomapp.models import *

def index(request):
    return render(request, 'index.html')

def add_product(request):
    if request.method == 'POST':
        hide = request.POST.get('hide')
        if hide == 'hide':
            category = request.POST.get('category')
            Category.objects.create(c_name = category)
        else:
            product_name = request.POST.get('product_name')
            product_description = request.POST.get('product_description')
            product_price = request.POST.get('product_price')
            product_image = request.FILES.get('product_image')
            avail_stk =  request.POST.get('product_stock')
            catgry = request.POST.get('category')

            ctg = Category.objects.filter(c_name =  catgry).first()

            Product.objects.create(name = product_name, description = product_description, price = product_price, image = product_image, stk_available = avail_stk, category =  ctg)

    categories =  Category.objects.all()
    context = {'category' :  categories}

    return render(request,  'add_product.html', context)


def products(request):
    if request.method == 'POST':  
        cartitem_id = request.POST.get('cartitem')
        product = Product.objects.filter(id=cartitem_id).first()

        if product:
            cartitem = Cartitems.objects.all().first()
            if cartitem:
                print(cartitem.item.first().name)
                cartitem.item.add(product) 
            else:
                ctitem = Cartitems.objects.create()
                ctitem.item.add(product)
    prod = Product.objects.all()
    categ = Category.objects.all()
    context = {
        'products' : prod,
        'categories' : categ,
    }
    return render(request, 'products.html', context)

def checkout(request, id):
    prodcts = Product.objects.filter(id = id).first()
    context = {
        'prodcts'  : prodcts,

    }
    return render(request, 'checkout.html', context)

def cartitems(request):
    if request.method == 'POST':
        hidden = request.POST.get('hidden')
        if hidden == 'hidden':
            deleteid = request.POST.get('deleteid')
            cartitem = Cartitems.objects.all().first()
            m = cartitem.item.filter(id = deleteid).first()
            cartitem.item.remove(m)
        else:
            Quantity =  request.POST.get('Quantity')
            cartitemss = Cartitems.objects.all().first()
            order = cartitemss.item.all()
            Cartitems.objects.all().first().delete()
            return redirect('products')

    cartitems = Cartitems.objects.all().first()
    if cartitems:
        crt =  cartitems.item.all()
    else:
        crt = None
        cartitems = None

    context = {
        'cartitems' : cartitems,
        'crt' : crt,
        }
    return render(request, 'cartitems.html', context)