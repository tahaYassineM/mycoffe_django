from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def products(request):

    context = {}
    products = Product.objects.all()

    if 'cs' in request.GET:
        cs = request.GET['cs']
        if not cs:
            cs = 'off'

    if 'searchname' in request.GET:
        name = request.GET['searchname']

        if name:
            if cs == 'on':
                products = products.filter(name__contains=name)
            else:
                products = products.filter(name__icontains=name)

    if 'searchdesc' in request.GET:
        searchdesc = request.GET['searchdesc']

        if searchdesc:
            if cs == 'on':
                products = products.filter(description__contains=searchdesc)
            else:
                products = products.filter(description__icontains=searchdesc)

    if 'searchpricefrom' in request.GET and 'searchpriceto' in request.GET:
        pricefrom = request.GET['searchpricefrom']
        priceto = request.GET['searchpriceto']

        if pricefrom and priceto:
            if pricefrom.isdigit() and priceto.isdigit():
                products = products.filter(
                    price__gte=pricefrom, price__lte=priceto)

    context['products'] = products

    return render(request, 'products/products.html', context)


def product(request, prod_id):
    context = {
        'product': get_object_or_404(Product, pk=prod_id)
    }
    return render(request, 'products/product.html', context)


def search(request):
    return render(request, 'products/search.html')
