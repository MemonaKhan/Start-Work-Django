from django.shortcuts import render
from django import forms            # for django forms

class NewTasksForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


# Create your views here.

tasks = ["abc","foo","bar"]
def index(request):
    return render(request,"taskstodo/index.html",{
        "tasks":tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTasksForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request,"taskstodo/add.html",{
                "form" : form
            })
    return render(request,"taskstodo/add.html",{
        "form" : NewTasksForm()
    })