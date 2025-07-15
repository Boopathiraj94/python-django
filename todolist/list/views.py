from django.shortcuts import redirect, render
from .models import Lists
# Create your views here.

def todolist(request):
    all_lists = Lists.objects.all()
    if all_lists:
        return render(request,'index.html',{'lists':all_lists})
    else:
        return render(request,'index.html')
    

def save(request):
    # print(request.method)
    if request.method == "POST":
       mes =  request.POST.get("messages")
       isSave = Lists.objects.create(messages=mes)
       isSave.save()
       return redirect('todolist')
    
def delete(request,id):
    list = Lists.objects.get(id=id)
    list.delete()
    return redirect('todolist')
      
def update(request,id):
    list = Lists.objects.get(id=id)
    return render(request,'update.html',{'list':list})

def update_form(request,id):
    # print(request.method)
    list = Lists.objects.get(id=id)
    if request.method == "POST":
        mes =  request.POST.get("messages")
        list.messages = mes
        list.save()
        return redirect('todolist')



# let obj ={
#     "message":"hi",
#     "name":"siva"
# }

# console.log(obj.name)

# obj.name = "raja"