from django.shortcuts import render

# Create your views here.

tasks = ["abc","foo","bar"]
def index(request):
    return render(request,"taskstodo/index.html",{
        "tasks":tasks
    })

def add(request):
    return render(request,"taskstodo/add.html")