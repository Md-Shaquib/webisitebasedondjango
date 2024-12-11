from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from .models import Product
# Create your views here.
def home(requests,*args,**kwargs):
    obj = Product.objects.get(id=1)
    my_context ={
        "object":obj
    }
    return render(requests,"home/home.html",my_context)

def create_home(requests,*args,**kwargs):
    form = ProductForm(requests.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()
    my_context ={
        "form":form
    }
    return render(requests,"home/home_create.html",my_context)

def delete_home(request,id):
    obj = get_object_or_404(Product,id=id)
    if request.method == "POST":
        obj.delete()
    context = {
        "object":obj
    }
    return render(request,"home/home_delete.html",context)