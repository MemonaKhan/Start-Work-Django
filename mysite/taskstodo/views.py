from django.shortcuts import render
from django import forms            # for django forms
from django.http import HttpResponseRedirect    # for redirecting page
from django.urls import reverse     # for redirecting page

class NewTasksForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.

# tasks = ["abc","foo","bar"]
# tasks = []                    #removed it bcz of sessions
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request,"taskstodo/index.html",{
        # "tasks":tasks                                   #removed bcz of session
        "tasks":request.session["tasks"]           # got error here so run command python manage.py migrate
    })

def add(request):
    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task)                 # used when using global variable
            request.session["tasks"] += [task]               # use it when using session
            return HttpResponseRedirect(reverse("viewtasks"))  # but after giving appname use tasks:index here
        else:
            return render(request,"taskstodo/add.html",{
                "form" : form
            })
    return render(request,"taskstodo/add.html",{
        "form" : NewTasksForm()
    })