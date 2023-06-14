from django.shortcuts import render
from product.models import Product,Reviews
# Create your views here.

def list(request):
    product_list = Product.objects.all()
    context={'product_list':product_list}
    return render(request,'list.html', context)


def details(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    return render(request,'details.html',context)