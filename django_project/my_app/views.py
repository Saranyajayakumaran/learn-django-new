from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request,"home.html")

def product(request):
    mobile=int(request.GET["mobile"])
    keyboard=int(request.GET["keyboard"])
    monitor=int(request.GET["monitor"])
    price=mobile+keyboard+monitor
    return render(request,"result.html",{'price':price})