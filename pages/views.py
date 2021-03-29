from django.shortcuts import render
from products.models import Product
# Create your views here.


def index(request):
    context = {
        'products': Product.objects.all()[:6]
    }

    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html', {})


def coffee(request):
    return render(request, 'pages/coffee.html', {})
