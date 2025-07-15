from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Loginss
# Create your views here.

def login(request):
    return render(request,'')
    #return HttpResponse("sdfs")

def register(request):
    if request.method == 'POST':
        fn=request.POST.get('firstName')
        ln = request.POST.get('lastName')
        un = request.POST.get('userName')
        # print(fn,ln,un)
        try:
            #isRegiter = Loginss.objects.create(first_name=fn,last_name=ln,user_name=un)
            isRegiter = Loginss(first_name=fn,last_name=ln,user_name=un)
            # isRegiter.save()
            # return HttpResponse(request, 'sdfsdf')
             
            isRegiter.save()
            # return redirect('book_list')
        
        except Loginss.DoesNotExist:
            print("error",Loginss)
            
        
    return render(request,'index.html')