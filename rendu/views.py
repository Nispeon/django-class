from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, response, Http404, HttpResponseRedirect

from .models import Product
from django.utils import timezone

from .forms import productform


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def create(request):
    if request.method == "POST":
        product = Product.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            image=request.POST['image'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
        )
        product.save()
    return redirect('/')


def show(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.quantity <= 0:
        return redirect('/')
    return render(request, 'show.html', {'product': product})


def cart(request, id):
    quantity = request.POST['quantity']
    product = get_object_or_404(Product, pk=id)
    product.quantity -= int(quantity)
    product.save()
    return redirect('/')
