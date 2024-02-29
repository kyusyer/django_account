from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="task")

# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {"tasks":request.session["tasks"]})


def addtasks(request):
    if request.method=="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
        return HttpResponseRedirect(reverse("tasks:index"))
    return render(request, "tasks/addtasks.html", {"form":NewTaskForm()})