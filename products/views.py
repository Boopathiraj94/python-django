from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
# Create your views here.

def index(request):
    if request.method == 'POST':
        pn = request.POST.get('productname')
        rate = float(request.POST.get('rate'))
        s = int(request.POST.get('stock'))
        # s = Products(obj)
        #isRegiter = Products.objects.create(product_name=pn,rate=rate,stock=s)
        isRegiter = Products(product_name=pn,rate=rate,stock=s).save()
        return HttpResponse("Saved")


    return render(request,'products.html')
