from django.shortcuts import render, HttpResponseRedirect
from .models import Product
from .forms import ProductForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        fm=ProductForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['desc']
            pw = fm.cleaned_data['price']
            reg = Product(name=nm,desc=em,price=pw)
            reg.save()
            fm=ProductForm() #clear the form
    else:
         fm = ProductForm() #initialize the form

    prod = Product.objects.all()#fetching all data
    return render(request,"clothing/home.html",{"prod":prod, "fm":fm})

def update_data(request,id):
    if request.method == 'POST':
        pi=Product.objects.get(pk=id)
        fm=ProductForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Product.objects.get(pk=id)
        fm=ProductForm(instance=pi)
    
    return render(request, 'clothing/update.html',{'form':fm})

def delete_data(request,id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')