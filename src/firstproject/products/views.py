from django.shortcuts import render
from .models import product
from .forms import product_form
# Create your views here.
def product_detail_view(request):
    obj = product.objects.get(id=1)
    context = {
        'object' : obj
    }
    return render(request, "product/detail.html",context)


def product_create_view(request):
    form = product_form(request.POST or None)
    
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form
    }
    return render(request, "product/product_create.html",context)