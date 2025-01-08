from django.shortcuts import render
from .models import Product, Category, Order

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/products.html', context)