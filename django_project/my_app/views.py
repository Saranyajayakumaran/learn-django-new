from django.shortcuts import render
from django.http import HttpResponse
from .models import Datas



# Create your views here.
def home(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request,'home.html',{'datas':mydata})
    else:
        return render(request,'home.html')
   
def addData(request):
     if request.method== 'POST' :
        name=request.POST.get('name')
        age=request.POST.get('age')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        email=request.POST.get('email')


        if not all([name, age, address, contact, email]):
            error_message = "All fields are required."
            return render(request, "home.html", {"error": error_message})

        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Email=email
        obj.save()

        mydata=Datas.objects.all()
        return redirect('home')
     return render(request,"home.html")