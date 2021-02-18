from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello From Memona Khan")    # initial line

def home(request):
    return render(request,"home/index.html")         # render content from template/home/index.html
def name(request):
    return HttpResponse("<h1>Hello here from name</h1>")    # render html content

def greet(request,name):
    return HttpResponse(f"Hello! {name.capitalize()}")         #render content from url get input

def page(request,name):
    return render(request,"page/index.html",{                  #render html file but also give data
        "name":name.capitalize()
    })