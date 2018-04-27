from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Product, Category


def index(request):
    # header_str = 'hello, p4 variable'
    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'keyboard.html', context)


def category(request, category_id):
    # category = Category.objects.get(id=category_id)
    context = {
        'products': Product.objects.filter(category__id=category_id),
        'categories': Category.objects.all()
    }

    return render(request, 'keyboard.html', context)

def insert_product():
    return

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('home')